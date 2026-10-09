from ultralytics import YOLO 

model = YOLO("nikita1.pt")
model.export(format="onnx")