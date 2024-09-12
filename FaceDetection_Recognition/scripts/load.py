
import numpy as np
from keras_facenet import FaceNet
from faceloading import FACELOADING 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

class Load_NPZ:
    def __init__(self):
        self.X = []
        self.Y = []
        self.EMBEDDED_X = []
        self.embeder = FaceNet()
        faceDataset = FACELOADING("facenetData")
        self.X, self.Y = faceDataset.load_classes()
       

    def get_embedding(self, face_img):
        face_img = face_img.astype('float32')
        face_img = np.expand_dims(face_img, axis=0)

        yhat = self.embeder.embeddings(face_img)
        return yhat[0]
    
    def npz(self, img):
        for img in self.X:
            self.EMBEDDED_X.append(self.get_embedding(img))

        EMBEDDED_X = np.asarray(EMBEDDED_X)

        np.savez_compressed('faces_embeddings_done_4classes.npz', EMBEDDED_X, self.Y)
        return EMBEDDED_X

    def birsey(self):
        encoder = LabelEncoder()
        encoder.fit(self.Y)
        self.Y = encoder.transform(self.Y)
        self.vector_train()

    def vector_train(self):
        X_train, X_test, Y_train, Y_test = train_test_split(self.EMBEDDED_X, self.Y, shuffle=True, random_state=17)
        model = SVC(kernel='linear', probability=True)
        model.fit(X_train, Y_train)
        ypreds_train = model.predict(X_train)
        ypreds_test = model.predict(X_test)
        accuracy_score(Y_train, ypreds_train)
        accuracy_score(Y_test,ypreds_test)

    def __call__(self):
        plt.figure(figsize=(16,12))
        for num,image in enumerate(self.X):
            ncols = 3
            nrows = len(self.Y)//ncols + 1
            plt.subplot(nrows,ncols,num+1)
            plt.imshow(image)
            plt.axis('off')
        self.birsey()
        
if __name__ == "__main__":
    load_npz = Load_NPZ() 
    load_npz()