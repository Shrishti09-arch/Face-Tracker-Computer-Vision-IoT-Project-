<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Face Tracker Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        ul {
            margin-left: 20px;
        }
        section {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>

<h1>Face Tracker 🎯</h1>

  <section>
        <h2>📌 Project Overview</h2>
        <p>
            The <strong>Face Tracker</strong> is a real-time computer vision and IoT-based project
            that detects and tracks human faces using a webcam and automatically follows the face
            movement using servo motors. The system combines Python-based face detection with
            Arduino-controlled pan and tilt mechanisms to achieve smooth and responsive tracking.
        </p>
    </section>

  <section>
        <h2>🚀 Features</h2>
        <ul>
            <li>Real-time face detection using a webcam</li>
            <li>Accurate face tracking with smooth pan and tilt motion</li>
            <li>Automatic servo motor control based on face position</li>
            <li>Python–Arduino synchronization for hardware control</li>
            <li>Efficient and lightweight implementation</li>
        </ul>
    </section>

  <section>
        <h2>🛠️ Technologies Used</h2>
        <ul>
            <li>Python</li>
            <li>OpenCV</li>
            <li>CVZone</li>
            <li>Arduino Uno</li>
            <li>Servo Motors</li>
            <li>PyFirmata</li>
            <li>Computer Vision</li>
            <li>IoT</li>
        </ul>
    </section>

  <section>
        <h2>⚙️ How It Works</h2>
        <ol>
            <li>The webcam captures live video input.</li>
            <li>OpenCV and CVZone detect the face in each frame.</li>
            <li>The face position is calculated relative to the frame center.</li>
            <li>Python sends position data to Arduino using PyFirmata.</li>
            <li>Servo motors adjust their angles to keep the face centered using pan and tilt movement.</li>
        </ol>
    </section>

  <section>
        <h2>🔌 Hardware Requirements</h2>
        <ul>
            <li>Arduino Uno</li>
            <li>2 Servo Motors (Pan & Tilt)</li>
            <li>Webcam</li>
            <li>Breadboard & Jumper Wires</li>
            <li>USB Cable</li>
        </ul>
    </section>

  <section>
        <h2>💻 Software Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Arduino IDE</li>
            <li>OpenCV</li>
            <li>CVZone</li>
            <li>PyFirmata</li>
        </ul>
    </section>

  <section>
        <h2>▶️ Usage</h2>
        <ol>
            <li>Upload <strong>StandardFirmata</strong> to Arduino using Arduino IDE.</li>
            <li>Connect the servo motors to the Arduino.</li>
            <li>Run the Python script.</li>
            <li>Place your face in front of the webcam and observe real-time tracking.</li>
        </ol>
    </section>

  <section>
        <h2>📈 Applications</h2>
        <ul>
            <li>Surveillance systems</li>
            <li>Robotics and automation</li>
            <li>Smart cameras</li>
            <li>Human–computer interaction</li>
            <li>Security and monitoring systems</li>
        </ul>
    </section>

  <section>
        <h2>📚 Learning Outcomes</h2>
        <ul>
            <li>Hands-on experience with computer vision</li>
            <li>Python–Arduino hardware integration</li>
            <li>Real-time data processing</li>
            <li>Servo motor control and automation</li>
        </ul>
    </section>

  <section>
        <h2>👤 Author</h2>
        <p><strong>Shrishti Vaishnav</strong></p>
    </section>

</body>
</html>





