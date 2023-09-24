# 6. Video Streaming App
# We need to install opencv-python library

from flask import Flask, render_template, url_for, Response
import cv2

app = Flask(__name__)

# Capture our camera
camera = cv2.VideoCapture(0)
# For remote webcam streaming we need to use IP address, username and password of that system device/camera

def generate_frames():
    """
        Video streaming generator function.
    """
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # we have to imencode frame to jpg format
            ret, buffer = cv2.imencode('.jpg', frame)  # encode the frame in JPEG format
            # Convert the image to bytes and send it as an HTTP response in the multipart/x-mixed-replace format
            frame = buffer.tobytes()
            # yeild keyword is used to return the value from the function
            yield (b'--frame\r\n'
                b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')   # concat frame one by one and show result

@app.route('/')
def index():
    """
        Home page
    """
    return render_template('index.html')

@app.route('/video')
def video():
    """
        Video streaming route. Put this in the src attribute of an img tag
    """
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
