from ultralytics import YOLO
import numpy as np
import torch
import cv2
from time import time
from roboflow import Roboflow

class ObjectDetectionCode:
    def __init__(self, caputure_index):
        self.caputure_index = caputure_index

        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("usin device: ", self.device)

        # self.load_dataset =self.load_dataset()
        self.model = self.load_model()

    # Roboflow API'sini kullanarak bir veri seti indirme
    def load_dataset(self):
        rf = Roboflow(api_key="nEhp8cbjBgoNgJwDJFYQ")
        project = rf.workspace("ws-sknfg").project("humanface-kkjiu")
        version = project.version(3)
        dataset = version.download("yolov8")
                
    # Modelin yüklenmesi ve egitimi      
    def load_model(self):
        model = YOLO('v10_180.pt')
        model.train(data='C:/Users/CaglaOkmen/projeYolo/humanface-3/data.yaml', epochs= 100, imgsz= 640)
       # model.val()
        return(model)

    # Gelen resimlerin model üzerindeki tahminleri
    def predict(self, frame):
        results = self.model(frame)
        return results
    
    # Tahmin edilen sonuclari gosterir
    def plot_boxes(self, results, frame):
        xyxys = []
        confidences = []
        class_ids = []
        for result in results:
            boxes = result.boxes.cpu().numpy()
          #  xyxys = boxes.xyxy
           # for xyxy in xyxys:
            #    cv2.rectangle(frame, int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3]), (0,255,0), 2)
            xyxys.append(boxes.xyxy) # Kutu kordinatları
            confidences.append(boxes.conf) # Guven degerleri
            class_ids.append(boxes.cls) # Class etiketleri

        return results[0].plot(), xyxys, confidences, class_ids

    def __call__(self):
        cap = cv2.VideoCapture(self.caputure_index)
        assert cap.isOpened(), "Kamera açılamadı!"
        
        # Kameranın çözünürlüğünü ayarlama
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Görüntü yakalanamadı!")
                break

            # Başlangıç zamanını kaydet (FPS hesaplamak için)
            start_time = time()

            # Model ile tahmin yap
            results = self.predict(frame)

            # Tahmin sonuçlarına göre sınır kutuları ve diğer bilgileri ekrana çiz
            frame, xyxys, confidences, class_ids = self.plot_boxes(results, frame)

            # Ekranda görüntüyü göster
            cv2.imshow("YOLO Tahmin", frame)

            # FPS hesapla ve ekrana yazdır
            end_time = time()
            fps = 1 / (end_time - start_time)
            print(f"FPS: {fps:.2f}")

            # 'q' tuşuna basıldığında döngüden çık
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Kaynakları serbest bırak
        cap.release()
        cv2.destroyAllWindows()


# Kodun çalıştırılması
if __name__ == "__main__":
    detection_code = ObjectDetectionCode(0)  # 0, varsayılan kamera
    detection_code()