# IArchitectonic (Architectonic Style Identifier with an IA) 

This project has been developed as final assignment of the machine learning bootcamp of Core-Code school.
The aim of this project is to develop a machine learning code which can identify the architectonic style of a building just with a picture of your phone.

## PROJECT STAGES
This project has been divided in some steps in order to organize the workload

1-	Organize and prepare the DATASET.

2-	Try and fit some machine learning models to select the most adequate for this kind of project.

3-	Create an API in python connected to a DataBase to feed the model

4-	Create an Streamlit page to present the data from the API.

5-	Dockerize the code in Google Cloud to be sure that always is working

### 1- DATASET PREPARATION

The Dataset of this project can be downloaded from kaggle: https://www.kaggle.com/datasets/dumitrux/architectural-styles-dataset?resource=download. It contains 10113 pictures divided in 25 folders, each one corresponds to a different  architectural style (from Achaemenid and Ancient Egyptian architecture to Postmodern architecture). 

To avoid overloading of the model, it has only been used 5 styles to train the model: 
- Postmodern
- Novelty
- International style
- Deconstructivism 
- Chicago School architecture

After having a trained model, it is going to be added other styles.

###2 -MACHINE LEARNING MODEL

