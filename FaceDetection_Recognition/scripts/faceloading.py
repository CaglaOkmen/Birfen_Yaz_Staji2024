import numpy as np
import os
import cv2
import matplotlib.pyplot as plt

class FACELOADING:
    def __init__(self, directory):
        self.directory = directory
        self.target_size = (160, 160)  # Hedef boyut
        self.X = []
        self.Y = []

    def resize_face(self, image):
        return cv2.resize(image, self.target_size)

    def load_faces(self, dir):
        FACES = []
        for im_name in os.listdir(dir):
            try:
                path = os.path.join(dir, im_name)
                face = cv2.imread(path)
                if face is not None:
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)  # Renk dönüşümü
                    face_resized = self.resize_face(face)  # Boyutlandırma
                    FACES.append(face_resized)
            except Exception as e:
                print(f"Error loading image {im_name}: {e}")
        return FACES

    def load_classes(self):
        for sub_dir in os.listdir(self.directory):
            path = os.path.join(self.directory, sub_dir)
            if os.path.isdir(path):
                FACES = self.load_faces(path)
                labels = [sub_dir for _ in range(len(FACES))]
                print(f"Loaded successfully: {len(labels)} images from class {sub_dir}")
                self.X.extend(FACES)
                self.Y.extend(labels)
        
        return np.asarray(self.X), np.asarray(self.Y)

    def plot_images(self):
        plt.figure(figsize=(18,16))
        for num, image in enumerate(self.X):
            ncols = 3
            nrows = len(self.X) // ncols + 1
            plt.subplot(nrows, ncols, num + 1)
            plt.imshow(image)
            plt.axis('off')
        plt.show()
