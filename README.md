# MTL_MRCNN for Object Detection, Segmentation, and Attribute extraction
This model is a multitask object detection model, developed on top of MRCNN model.This model detect objects within the images, perform segmentation and extract meaningful attribute from the image. The model is validated on head detection and pose estimation.  

This repository includes:
* Source codes of MTL_MRCNN, built on Mask Regional CNN (MRCNN)
* The trained weight for head detection and pose estimation (Trained on Prima dataset)
* Jupyter notebook for donwloading the images and splitting the dataset
* Jupyter notbooks for training and inference

# Getting Started
For training your own model, follows the instruction below:
1. Generate a jointly annotated dataset (in COCO format with .JSON extention). The dataset contains the objects class annotation, segmentation and attributes. You can use www.ai-console.com for this.
2. Rename the dataset to dataset.json and replace it with the one in the main directory.
3. Open the Config_default.ini and set the directories and parameters.
4- Run the Dataset.ipynb jupyter notebook to download the images on your local machine and also spliting the dataset.
5- Download the pre-trained COCO weight from here, and plce it in your ../files/logs directory.
6- Open the Train.ipynp script, change the hyperparamerts at Shapeconfig class if needed, and run the script.

# Age Estimation
Our model is tested in the UTKFace dataset, for face detection and age estimation. 

![image](https://user-images.githubusercontent.com/45915632/150688616-bd134d70-2966-4358-b8ba-8dab1d6d3a7a.png)
