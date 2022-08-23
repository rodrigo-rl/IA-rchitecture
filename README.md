![Architecture](https://user-images.githubusercontent.com/101878865/185236283-eb2187f0-0154-41cf-9727-3be28737e9d3.gif)

# IA rchitecture (Architectural Style Identifier with an IA) 

This project has been developed as final assignment of the machine learning bootcamp of Core-Code school.
The aim of this project is to develop a machine learning code which can identify the architectonic style of a building just with a picture.

The 1.0 version can be found on-line in this direction: https://architectural.herokuapp.com/

## Project Stages
This project has been divided in some steps in order to organize the workload.

<details><summary>1-	Organize and prepare the DATASET.</summary>

The Dataset of this project can be downloaded from kaggle: https://www.kaggle.com/datasets/dumitrux/architectural-styles-dataset?resource=download. It contains 10113 pictures divided in 25 folders, each one corresponds to a different  architectural style (from Achaemenid and Ancient Egyptian architecture to Postmodern architecture). 

To avoid overloading of the model, it has only been used 5 styles to train the model: 
- Postmodern
- Novelty
- International style
- Deconstructivism 
- Chicago School architecture

After having a trained model, it is going to be added other styles to distinguish more styles.

</details>

<details><summary>2-	Try and fit some machine learning models to select the most adequate for this kind of project.</summary>

The model selected to us in this application is a derived model from “ResNet50” where are added a Flattern layer, a Dense layer with 512 units and “relu” activation and a Dense layer with 5 units and “softmax” activation (based on this article of a similar problem: https://chroniclesofai.com/transfer-learning-with-keras-resnet-50/). 

ResNet50 is a very well known CNN model which can be found in the paper by K. He et al. (publised in 2017): Deep Residual Learning for Image Recognition (https://arxiv.org/abs/1512.03385). This CNN model was development to solve the degradation problem in a deep network (adding more layers to a sufficiently deep neural network would first see saturation in accuracy and then the accuracy degrades).

The current model has reach an accuracy higher than 80% as can be seen in the picture of the next chapter.

</details>

<details><summary>3-	Create an API in python connected to MongoDB to feed the model.</summary>

It has been created a Data Base in MongoDB with pictures and information of the buildings of each architectural styles (Authors, Year of construction and Name of the building). This Data Base has been dockerized and published in Heroku to be available at any time.

![Mongo](https://user-images.githubusercontent.com/101878865/185746418-56d9652c-91fa-4909-b002-cfc87bda2a05.jpg)

</details>

<details><summary>4-	Create an Streamlit page to present the results.</summary>

A Streamlit web has been developed to present all the data. There site is divided in two pages, the first one to explain how all the things works and the other one where all the magic happens (see next picture). 

![Streamlit-nothing](https://user-images.githubusercontent.com/101878865/185240943-52c804a0-b378-4420-9775-c99d0ad86954.jpg)

When an image is uploaded and confirmed, the model starts looking for similarities to stablishs the most probable architectural style and to presents the result. After that, the program calls (through the API) to a MongoDB data base where can be found pictures and information of buildings of the same style.

![Streamlit-Results](https://user-images.githubusercontent.com/101878865/185236400-c42ce73a-e7c0-45f4-b3a0-2219cb46a8c3.jpg)

</details>

<details><summary>5-	Next steps.</summary>


It has been identified two main paths to improve this project:

- Add more styles to make more complete and complex the model.
- Add this project to Google Cloud to be sure that there is not faillure in the website if there are a lot of users. 

</details>

## Mode of Use

asdas

## Installation

There are three folders that compose the whole project:
- Data_base
- API
- streamlit

Depending on what do you want to do, it isn't neccesary to download all the files. 

### Data_base

**Data_Base** folder allows to add more information to the Building Information Data Base (I have stored the information in MongoDB but can be used another Data Base). To add more information, it is necessary to:

- 1 Fulfil the excel file *Buildings.xls* with the same structure and add the picture in the folder */Data_base/example/<name_style>*.
- 2 Run in Jupyter Notebook *DATA_BASE Creation-GH.ipynb* <sub>(warning: paths can change depending your folder structure)</sub>

*DataBase of cnn model-GH.ipynb* it is used to storage new versions of the model (the idea is to be able calling the newst model from the data base through the API, I am currently study this possibility). 

### API

**API** folder contains all the code neccesary to connect the MongoDB database to streamlit and the files to create a docker version to deploy in a pltafform like *Heroku*. *Main.py* is the API main file and inside of them there are the files of the three endpoints used in the project (which correspond to a file of **routers** folder):

- *Styles.py* --> This file defines the endpoint to obtain the information of the building (name, architect, picture...). It select 3

### streamlit

The trained model can be found in this google drive folder: https://drive.google.com/drive/folders/1-A6qfB4NOYQYKniJ0aHphFf2uez9ZsB8?usp=sharing
To use it you should download it and paste in the following path: **streamlit/Model/** 

To install and use the project, you have to download the **streamlit** folder and run it with the following line code: 

```ruby
   streamlit run Presentation.py
```

To add more information (buildings or new styles) in the data_base, download **Data_base** folder and use Jupyter notebook to do that (the URL has been deleted, contact with me to upload new information please!)

To make modifications in the API, you can find all of the code inside **API** folder, where the endoints can be modificated as your wish.

## Acknowledgment

I want to thank you all the members of Core Code School and especially to the proffersors Marc Pomar, Alvaro Lucas Cueva, Santino Lede and Daniel Alvarado for all the things that have teached me during the course.   
