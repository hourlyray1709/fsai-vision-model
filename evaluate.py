from ultralytics import YOLO 
from pathlib import Path
from datetime import datetime 

# path constants, you should change these to match your system 
fsoco_path = "fsoco_bounding_boxes_train"
yolo_path = "fsoco_bounding_boxes_train_yolo"

model = YOLO("nikita1.pt")

def inference(): 
    path_to_images = yolo_path + "/images/train"
    result = model(path_to_images, imgsz=320, stream=True, save=True)
    return result

start = datetime.now() 
result = inference() 
end = datetime.now() 

size = 0 
for i in result: 
    size += 1 

delta = end - start
ms = delta.total_seconds() * 1000
print(delta / size)
