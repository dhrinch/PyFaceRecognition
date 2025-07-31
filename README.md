# Face Recognition Attendance System

A real-time face recognition system that automatically marks attendance using your webcam. The system compares detected faces against a database of known individuals and logs their attendance with timestamps.

## Features

- **Real-time face detection** using webcam feed
- **Automatic attendance marking** with timestamp logging  
- **Multiple face recognition** in single frame
- **CSV-based attendance logging** for easy data management
- **Visual feedback** with bounding boxes and names
- **Duplicate prevention** - marks attendance only once per session

## Requirements

### Python Dependencies

```bash
pip install opencv-python numpy face-recognition
```

### Hardware Requirements

- Webcam or camera device
- Good lighting conditions for optimal face detection

## Installation

1. **Clone or download** this project to your local machine

2. **Install required packages:**
   ```bash
   pip install opencv-python numpy face-recognition
   ```

3. **Create the image directory:**
   ```bash
   mkdir ImagesAttendance
   ```

4. **Add reference photos** to the `ImagesAttendance` folder:
   - Use clear, well-lit photos showing one face per image
   - Supported formats: `JPG`, `JPEG`, `PNG`, `BMP`
   - Name files with the person's name (e.g., `john_doe.jpg`)

## Usage

1. **Prepare reference images:**
   - Place clear photos of people in the `ImagesAttendance` folder
   - One face per image, good lighting, front-facing
   - File names become the attendance names

2. **Run the system:**
   ```bash
   python AttendanceProject.py
   ```

3. **Using the system:**
   - The webcam window will open showing the live feed
   - When a known face is detected, a rectangle appears with the person's name
   - Attendance is automatically logged to `Attendance.csv`
   - Press **'q'** or **ESC** to quit the application

## File Structure

```
PyFaceRecognition/
├── AttendanceProject.py     # Main application file
├── ImagesAttendance/        # Directory for reference photos
│   ├── person1.jpg
│   ├── person2.jpg
│   └── ...
├── Attendance.csv           # Generated attendance log
└── README.md               # This file
```

## Output

The system generates `Attendance.csv` with the following format:

```csv
Name,Time
JOHN DOE,14:30:25
JANE SMITH,14:32:18
```

## Troubleshooting

### Common Issues

**"No face found in image"**
- Ensure reference images have clear, visible faces
- Use well-lit photos taken from the front
- One person per image

**"Camera not working"**
- Check if another application is using the camera
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` for different camera

**"Poor recognition accuracy"**
- Improve lighting conditions
- Use higher quality reference images
- Ensure faces are clearly visible and not blurry

**"Directory not found"**
- Make sure `ImagesAttendance` folder exists in the same directory as the script
- Check that image files are in the correct format (`JPG`, `PNG`, etc.)

### Performance Tips

- Use smaller images for faster processing
- Ensure good lighting for better accuracy
- Keep reference images under 1MB for faster loading
- Close other camera applications before running

## Technical Details

- **Face Detection**: Uses HOG (Histogram of Oriented Gradients) algorithm
- **Face Recognition**: 128-dimensional face encodings for comparison
- **Matching Threshold**: Configurable tolerance for face matching accuracy
- **Frame Processing**: Resizes frames to 25% for faster processing

## Known Limitations

- Requires good lighting conditions
- May struggle with extreme angles or partially obscured faces
- Performance depends on camera quality and processing power
- Single attendance entry per person per session

## Future Enhancements

- Database integration for better data management
- Web-based interface for remote monitoring
- Multi-camera support
- Enhanced reporting features
- Mobile app integration

## Dependencies Note

You may see a warning about `pkg_resources` being deprecated - this is harmless and doesn't affect functionality. It's from the face_recognition library and will be fixed in future updates.

## Support

For issues or questions:

1. Check the troubleshooting section above
2. Ensure all dependencies are correctly installed
3. Verify your Python version compatibility
4. Test with high-quality reference images

---

**Note**: This system is designed for controlled environments with good lighting and clear face visibility for optimal performance.
