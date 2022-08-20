import requests
import pickle

def cnnmodel():
    
    aux=requests.get(f"https://ia-rchitecture.herokuapp.com/model").json()
    cnnmodel=pickle.loads(pickled_model)
 
    return cnnmodel

def school(school):

    aux=requests.get(f"https://ia-rchitecture.herokuapp.com/school/{school}").json()
    return aux

def name(name):

    aux=requests.get(f"https://ia-rchitecture.herokuapp.com/name/{name}").json()
    return aux
