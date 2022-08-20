![Architecture](https://user-images.githubusercontent.com/101878865/185236283-eb2187f0-0154-41cf-9727-3be28737e9d3.gif)

# IA rchitecture (Architectural Style Identifier with an IA) 

This project has been developed as final assignment of the machine learning bootcamp of Core-Code school.
The aim of this project is to develop a machine learning code which can identify the architectonic style of a building just with a picture.

## PROJECT STAGES
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


## Acknowledgment

I want to thank you all the members of Core Code School and especially to the proffersors Marc Pomar, Alvaro Lucas Cueva, Santino Lede and Daniel Alvarado for all the things that have teached me during the course.   
