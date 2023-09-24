# 7. Face & Eye Detection
# Learn: How to detect face and eye using Haar Cascade Classifier
# Haar Cascade Classifier:
#   - It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images.

from flask import Flask, render_template, Response
# Need to install opencv-python
import cv2


app=Flask(__name__)
camera = cv2.VideoCapture(0)


def generate_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # Create the haar cascade frontal face using the xml file and cascade classifier
            detector = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
            # Create the haar cascade eye using the xml file and cascade classifier
            eye_cascade = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')
            # Detect faces in the image
            faces = detector.detectMultiScale(frame,1.1,7)
            # Convert the image to gray scale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                # Create the rectangle around the face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                # Create the region of interest
                roi_gray = gray[y:y+h, x:x+w]
                # Create the region of interest color
                roi_color = frame[y:y+h, x:x+w]
                # Detect the eyes in the image
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
                # Draw the rectangle around each eye
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            # Convert the frame into bytes
            frame = buffer.tobytes()
            # Return the frame in the form of bytes
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=='__main__':
    app.run(debug=True)