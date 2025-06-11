import cv2
import os
import numpy as np

data_path = "dataset"
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_map = {}

label_id = 0
for user in os.listdir(data_path):
    user_dir = os.path.join(data_path, user)
    if not os.path.isdir(user_dir):
        continue
    label_map[label_id] = user
    for img_file in os.listdir(user_dir):
        img_path = os.path.join(user_dir, img_file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        faces.append(img)
        labels.append(label_id)
    label_id += 1

print("📚 Training face recognizer...")
face_recognizer.train(faces, np.array(labels))
face_recognizer.save("face_model.yml")
np.save("labels.npy", label_map)
print("✅ Model trained and saved as 'face_model.yml'")
