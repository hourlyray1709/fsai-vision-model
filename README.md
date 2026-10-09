# fsai-vision-model
University of Manchester Formula Student AI team repository to train our own Yolov8 model according to the FSOCO dataset

<h1>Prerequisites</h1>
<ul>
<li>Ultralytics</li>
<li>Supervisely</li>
<li>Run pip install ultralytics and pip install supervisely to install them</li>
</ul>


<h1>Convert Function</h1>
- Takes the path to the FSOCO dataset and turn it from supervisely to YAML format 

<h1>Split Function</h1>
<ul>
<li>Divide the YAML dataset into train test validate sets </li>
<li>IMPORTANT: Change the data_config.yaml in the yolo directory to use: 
    - train = "../fsoco_bounding_boxes_train_yolo/images/autosplit_train.txt" 
    and similarly for test and validate, 
    change the path to it appropriately. 
</li>
</ul>

<h1>Training the model</h1>
- Right now we are using the stock training parameters but you can tweak it if you want. 
