# MTL_MRCNN for Object Detection, Segmentation, and Attribute Extraction
This model is a multitask object detection model, developed on top of MRCNN model.This model detect objects within the images, perform segmentation and extract meaningful attribute from the image. The model is validated on head detection and pose estimation.  


![MTL_MRCNN](https://user-images.githubusercontent.com/45915632/169989388-5835f89a-75fb-445e-82e0-a9c0251a8313.png)




This repository includes:
* Source codes of MTL_MRCNN, built on Mask Regional CNN (MRCNN)
* The trained weight for head detection and pose estimation (Trained on Prima dataset)
* Jupyter notebook for donwloading the images and splitting the dataset
* Jupyter notbooks for training and inference

# Getting Started
For getting started, install the required packages as listed below:

- numpy
- scipy
- Pillow
- cython
- matplotlib
- scikit-image
- tensorflow>=1.3.0
- keras>=2.0.8
- opencv-python
- h5py
- imgaug
- pycocotool

For **training** your own model, follows the instruction below:
1. Generate a jointly annotated dataset (in COCO format with .JSON extention). The dataset contains the objects class annotation, segmentation and attributes. You can use www.ai-console.com for this.
2. Rename the dataset to dataset.json and replace it with the one in the main directory.
3. Open the Config_default.ini and set the directories and parameters.
4. Run the Dataset.ipynb jupyter notebook to download the images on your local machine and also spliting the dataset.
5. Download the pre-trained COCO weight from [here](https://www.mediafire.com/file/rhcz0oblz22fdrw/mask_rcnn_coco.h5/file), and plce it in your **../files/logs** directory.
6. Open the Train.ipynp script, change the hyperparamerts at Shapeconfig class if needed, and run the script.

For **running** the model follow the instruction below:
1. Place the weight file in the main directory.
2. Rename it to Weight.h5.
3. place the images those need to be inferred at **../images** folder.
4. Open the Run.ipynb script, set the hyperparamerts (e.g. _DETECTION_MIN_CONFIDENCE_) if needed, and then run the code.


# Examples
This model is tested for two challenges of age estimation and also head pose estimation. Three public datasets of _Prima_ and _BIWI_ (for head pose estimation), and _UTKFace_ for age estimation is used.
The weight of the trained model on _BIWI_ dataset is avaiable at [here](https://www.mediafire.com/file/k82dbxe2roxlu5v/Weight.h5/file).
For running the trained model, downlaod the weight file and follow the _running_ section as explained above.

* Some success example of the model on pose estimation on Prima and BIWI datasets.
![Pose](https://user-images.githubusercontent.com/45915632/151156639-3787c960-bfb0-4f31-a40a-0b9ca786e0b8.png)
