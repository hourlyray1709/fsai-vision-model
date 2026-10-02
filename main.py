from ultralytics import YOLO 
import supervisely as sly 
from ultralytics.data.split import autosplit

# path constants, you should change these to match your system 
fsoco_path = "fsoco_bounding_boxes_train"
yolo_path = "fsoco_bounding_boxes_train_yolo"

# do not change these unless you know what you're doing 
def convert(path): 
    # convert supervisely to yolo
    # path: the relative (to this python script) or absolute path to the supervisely dataset  
    project = sly.Project(path, sly.OpenMode.READ)
    project.to_yolo(yolo_path, task_type="detect")
    print("Finished yolo conversion")

def split(): 
    # split the yolo dataset into train test split 
    # after split, change train, test, val in the data_config.yaml to use autosplit_train.txt, etc. 
    # for example after split, in the yaml you should have train = ../fsoco_bounding_boxes_train_yolo/images/autosplit_train.txt if you do not change anything here 
    autosplit(
        path=yolo_path + "/images/train", 
        weights=(0.7, 0.2, 0.1),                                   # train test split ratio 
        annotated_only=True
    )

def train(yolo_model_name): # yolo_model_name: "yolov8n.t" | "yolo26m.pt" etc 
    # this will download the yolo model to your computer if you do not have it, make sure you have disk space 
    model = YOLO(yolo_model_name)
    model.train(data=yolo_path+"/data_config.yaml", epochs=100)        # optionally set cache=True if you have lots of ram to spare 
    model.export(format="onnx")


# main 
if __name__ == "__main__": 
    # feel free to change the workflow here. you may want to only convert to yolo and split once, and keep the result for training only 
    convert(fsoco_path)
    split() 
    # train("yolo26m.pt")  do not run the train until  you have changed data_config.yaml, see the readme