![Architecture](https://user-images.githubusercontent.com/101878865/185236283-eb2187f0-0154-41cf-9727-3be28737e9d3.gif)

# IA rchitecture (Architectural Style Identifier with an IA) 

This project has been developed as final assignment of the machine learning bootcamp of Core-Code school.
The aim of this project is to develop a machine learning code which can identify the architectonic style of a building just with a picture of your phone.

## PROJECT STAGES
This project has been divided in some steps in order to organize the workload

1-	Organize and prepare the DATASET.

2-	Try and fit some machine learning models to select the most adequate for this kind of project.

3-	Create an Streamlit page to present the results.

4-	Create an API in python connected to a DataBase to feed the model.

5-	Next steps
Dockerize the code in Google Cloud to be sure that always is working

### 1- DATASET PREPARATION

The Dataset of this project can be downloaded from kaggle: https://www.kaggle.com/datasets/dumitrux/architectural-styles-dataset?resource=download. It contains 10113 pictures divided in 25 folders, each one corresponds to a different  architectural style (from Achaemenid and Ancient Egyptian architecture to Postmodern architecture). 

To avoid overloading of the model, it has only been used 5 styles to train the model: 
- Postmodern
- Novelty
- International style
- Deconstructivism 
- Chicago School architecture

After having a trained model, it is going to be added other styles to distinguish more styles.

### 2- MACHINE LEARNING MODEL

The model selected to us in this application is a derived model from “ResNet50” where are added a Flattern layer, a Dense layer with 512 units and “relu” activation and a Dense layer with 5 units and “softmax” activation (based on this article of a similar problem: https://chroniclesofai.com/transfer-learning-with-keras-resnet-50/). 

ResNet50 is a very well known CNN model which can be found in the paper by K. He et al. (publised in 2017): Deep Residual Learning for Image Recognition (https://arxiv.org/abs/1512.03385). This CNN model was development to solve the degradation problem in a deep network (adding more layers to a sufficiently deep neural network would first see saturation in accuracy and then the accuracy degrades).

The current model has reach an accuracy higher than 80% as can be seen in the next picture.

### 3- Streamlit page

A Streamlit web has been developed to present all the data. There site is divided in two pages, the first one to explain how all the things works and the other one where all the magic happens. 

![Streamlit-nothing](https://user-images.githubusercontent.com/101878865/185240943-52c804a0-b378-4420-9775-c99d0ad86954.jpg)


When an image is uploaded and confirmed, the model starts to look for similarities to sablishs the most probable architectural style and present the result. After that, the program calls through an API to a data base where can be found pictures and information of buildings of the same style.  

![Streamlit-Results](https://user-images.githubusercontent.com/101878865/185236400-c42ce73a-e7c0-45f4-b3a0-2219cb46a8c3.jpg)

### 4 - API

It has been created a Data Base in MongoDB with some examples
