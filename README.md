# 🧠 Face Recognition System

A real-time face recognition application using Python, OpenCV, and the `face_recognition` library. This project captures facial data, stores it, and recognizes known users via an external USB/web camera.

## 📸 Features

- Real-time face detection and recognition
- Multi-face encoding and storage
- Recognizes faces from a secondary (external) camera
- Distance-based scanning and face tracking
- Access control logic (e.g., allow/deny)

## 🧰 Tech Stack

| Component      | Technology              |
|----------------|--------------------------|
| Language       | Python                   |
| Libraries      | OpenCV, face_recognition, NumPy |
| Hardware       | External USB camera (or laptop webcam) |
| Data Storage   | Image files with encoding (.pkl or .npy) |

## 🎯 Functional Workflow

1. **Capture Face Data:**
   - Captures and stores facial encodings from known users
   - Saves them locally in a serialized format

2. **Live Recognition:**
   - Reads video feed from external camera
   - Matches live frames with stored encodings
   - Displays identity on screen if matched

3. **Distance Filtering:**
   - Only starts recognition if the face is within a defined range (based on size/position)

## 📂 Project Structure

face-recognition/
├── known_faces/ # Stored face encodings
├── dataset/ # Captured images
├── face_encoder.py # Script to store new faces
├── recognize_live.py # Real-time recognition logic
├── utils.py # Helper functions (optional)
└── requirements.txt

shell
Copy
Edit

## ▶️ Getting Started

### 1. Install Dependencies

```bash
pip install opencv-python face_recognition numpy
2. Encode Your Face
bash
Copy
Edit
python face_encoder.py
# Stand still while your face is scanned
3. Start Recognition
bash
Copy
Edit
python recognize_live.py
# Ensure your external camera is connected
🔒 Security / Ethics
Facial data is stored locally (no external server).

Meant for personal or academic use only.

📌 Future Enhancements
Store encodings in a lightweight database

Add GUI using Tkinter or PyQt

Integrate with door lock or access systems

👨‍💻 Developed By
Uday Shastrakar
📧 uday.shastrakar@gmail.com
🌐 GitHub | Portfolio
