# Codes - 5 (Video Streaming Using Webcam) - Flask Tutorial | [Codes](../codes-5/) and [Docs](../docs/codes-5.md)

## Installation

```shell
pip install -r requirements.txt

or

pip install opencv-python
```

### `app.py`

```python
# write the below code in app.py file
from flask import Flask, render_template, redirect, url_for, Response
import cv2

app = Flask(__name__)
# Capture our camera
camera = cv2.VideoCapture(0)

# For remote video we need to use IP address, username and password of the system

def gen_frames():  
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # concat frame one by one and show result
            yield (b'--frame\r\n'
                b'Content-Type: image/jpg\r\n\r\n' + frame + b'\r\n')
    

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
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
```

### `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Streaming</title>
</head>
<body>
    <h1>Live Streaming</h1>
    <hr>
    <center>
        <div style="border: 3px solid;">
            <img src="{{ url_for('video') }}" width="50%" alt="Error">
        </div>
    </center>
</body>
</html>
```