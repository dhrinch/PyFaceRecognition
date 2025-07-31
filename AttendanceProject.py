import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImagesAttendance'
images = []
classNames = []

if not os.path.exists(path):
    print(f"Error: Directory '{path}' not found!")
    exit()

myList = os.listdir(path)
print(f"Found {len(myList)} files in '{path}'")

valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
myList = [f for f in myList if f.lower().endswith(valid_extensions)]

if not myList:
    print("Error: No valid image files found!")
    exit()

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    else:
        print(f"Warning: Could not load image {cl}")

def find_encodings(images):
    encode_list = []
    for i, img in enumerate(images):
        if img is None:
            print(f"Skipping None image at index {i}")
            continue
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img_rgb)[0]
        if len(encodings) > 0:
            encode_list.append(encodings)
        else:
            print(f"Warning: No face found in image {classNames[i] if i < len(classNames) else 'unknown'}")
    return encode_list

def mark_attendance(name):
    try:
        if not os.path.exists('Attendance.csv'):
            with open('Attendance.csv', 'w') as f:
                f.write('Name,Time\n')

        with open('Attendance.csv', 'r+') as f:
            my_data_list = f.readlines()
            name_list = []
            for line in my_data_list:
                entry = line.split(',')
                if len(entry) > 1:
                    name_list.append(entry[0])

            if name not in name_list:
                now = datetime.now()
                dt_string = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dt_string}')
                print(f"Marked attendance for {name} at {dt_string}")

    except Exception as e:
        print(f"Error marking attendance: {e}")

encodeListKnown = find_encodings(images)
print(f"Encoding complete, {len(encodeListKnown)} images processed")

if len(encodeListKnown) == 0:
    print("Error: No face encodings found! Check your reference images.")
    exit()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from camera")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    try:
        facesCurFrame = face_recognition.face_locations(imgS)
        if len(facesCurFrame) > 0:
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
                    cv2.putText(img, name, (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_COMPLEX,
                        1, (255, 0, 255), 2)
                    mark_attendance(name)
    except Exception as e:
        print(f"Error processing frame: {e}")
        continue

    cv2.imshow('Webcam', img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
