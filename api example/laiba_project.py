import cv2
import numpy as np
import sqlite3
import os

# Connect to the SQLite database
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Create the attendance table
c.execute('''CREATE TABLE IF NOT EXISTS attendance
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              date TEXT NOT NULL)''')

# Load the pre-trained Haarcascades model for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained face recognition model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the dataset and train the face recognition model
def train_face_recognizer():
    faces = []
    labels = []
    label_to_name = {}
    label = 0
    
    for name in os.listdir('dataset'):
        label_to_name[label] = name
        for filename in os.listdir(os.path.join('dataset', name)):
            img_path = os.path.join('dataset', name, filename)
            image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            faces.append(image)
            labels.append(label)
        label += 1
    
    face_recognizer.train(faces, np.array(labels))
    return label_to_name

# Mark attendance in the database
def mark_attendance(name):
    c.execute("INSERT INTO attendance (name, date) VALUES (?, DATE('now'))", (name,))
    conn.commit()

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Start face recognition
label_to_name = train_face_recognizer()
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        label, _ = face_recognizer.predict(face_roi)
        if label in label_to_name:
            name = label_to_name[label]
            mark_attendance(name)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('Automated Attendance System', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Close the database connection
conn.close()