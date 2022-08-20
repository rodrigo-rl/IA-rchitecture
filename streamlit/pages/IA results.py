def mach_learn (pict):# prediction
    #aux variables
    X_aux=[] 
    classes=["Postmodern style","Novelty architecture","International style", "Deconstructivism", "Chicago School of Architecture"]
    
    #creating classes
    enc=OneHotEncoder(handle_unknown='ignore')

    y=np.array(classes)
    y=y.reshape(-1,1)
    y_ohe=enc.fit_transform(y).toarray()

    # create an array with the right shape
    img=Image.open(pict).resize((200,200)).convert("L")
    g_img=np.expand_dims(img, axis=-1)
    g_img_chan=g_img.repeat(3, axis=-1)
    X_aux.append(g_img_chan)
    X_img=np.array(X_aux)
    print(f"g_img_chan.shape: {g_img_chan.shape}")
    print(f"X_img.shape: {X_img.shape}")

    model=keras.models.load_model("./Model/22_08_08-BN_pictures.h5")
    pred=model.predict(X_img)
    pred_text = enc.inverse_transform(pred)

    results=[pred_text, pred]
    return results

def picture(imagen,school,name): #to display picture and prediction results
    with Image.open(imagen) as image:
        image=image.convert("RGB")

        #select the most adequate way to present the picture (vertical/horizontal)
        if image.size[0]>image.size[1]:
            image=image.resize((350,250))
        else:
            image=image.resize((250,300))
    image=np.array(image)
    
    #display picture
    col1.image(image, caption="Uploaded picture")
    style=col2.empty()

    style.subheader("Thinking...")

    #display results
    solution=mach_learn(imagen)
    arch_sty=solution[0][0][0]
    style.header(arch_sty)
    col2.text("")

    conf= int(round(max(solution[1][0])*100, 0))
    col2.markdown(f"Percentage of confidence: **{round(max(solution[1][0])*100, 2)}%**")
    col2.progress(conf)
    col2.text("")


    #Wikipedia page
    boton=col2.button("Click me to go to the Wikipedia page")
    if boton==True:
        webbrowser.open_new_tab(Wiki(arch_sty))
    
    resultado1=school(arch_sty)
    st.subheader("Other buildings of the same style...")
    
    name1=resultado1[0]["Name"]
    arch1=resultado1[0]["Architects"]
    year1=resultado1[0]["Years"]
    image1 = blosc.unpack_array(base64.decodebytes(name(name1)['$binary'].encode()))
    
    name2=resultado1[1]["Name"]
    arch2=resultado1[1]["Architects"]
    year2=resultado1[1]["Years"]
    image2 = blosc.unpack_array(base64.decodebytes(name(name2)['$binary'].encode()))
    
    name3=resultado1[2]["Name"]
    arch3=resultado1[2]["Architects"]
    year3=resultado1[2]["Years"]
    image3 = blosc.unpack_array(base64.decodebytes(name(name3)['$binary'].encode()))

    col3, col4, col5 = st.columns(3)
    col3.image(image1)
    col3.text(f"Name: {name1}\nAuthor: {arch1}\nYear: {year1}")
    col4.image(image2)
    col4.text(f"Name: {name2}\nAuthor: {arch2}\nYear: {year2}")
    col5.image(image3)
    col5.text(f"Name: {name3}\nAuthor: {arch3}\nYear: {year3}")



def Wiki(arch_sty):#to obtain the link to the wiki page 
    if arch_sty=="Postmodern style":
        url="https://en.wikipedia.org/wiki/Postmodern_architecture"
    elif arch_sty=="Novelty architecture":
        url="https://en.wikipedia.org/wiki/Novelty_architecture"
    elif arch_sty=="International style":
        url="https://en.wikipedia.org/wiki/International_Style_(architecture)"
    elif arch_sty=="Deconstructivism":
        url="https://en.wikipedia.org/wiki/Deconstructivism"
    elif arch_sty=="Chicago school architecture":
        url="https://en.wikipedia.org/wiki/Chicago_school_(architecture)"
    
    return url

#libraries
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import OneHotEncoder
import webbrowser
import blosc
import base64
from pymongo import MongoClient

from data.get_data import cnnmodel, school, name
###-------------------------###
###  streamlit run main.py  ###
###-------------------------###

#title and description 
st.title('IA RESULTS')
st.subheader("")
#st.subheader('Upload a picture of a building to discover more about their style!') 

#to upload pictures
st.sidebar.header("Upload picture")
file=st.sidebar.empty()
file=st.sidebar.file_uploader("", type=["png","jpg"],accept_multiple_files=True)
load_data=st.sidebar.checkbox("Click me to upload the picture!")

#set the columns to present results
col1, col2 = st.columns(2)

if load_data==True:
    if file is not None:
        if len(file)==1:
            st.sidebar.success("Uploaded correctly")
            picture(file[0],school,name)
        elif len(file)>1:
            file=[file[len(file)-1]]
            picture(file[0],school,name)
    else:
        st.sidebar.error("Something went wrong")
