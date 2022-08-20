from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import APIRouter
import pickle
from json import loads
import os

router=APIRouter()

load_dotenv()
client=MongoClient(os.getenv("URL"))
db=client.get_database("Data")

@router.get("/model")
def get_models():
    #all the available models
    res=list(db["Cnn_model"].find())

    #look for the newest model
    solution=res[0]['creation']

    for i in range(len(res)):
        if res[i]['creation']>solution:
            solution=res[i]['creation']
    
    #select the newest model
    new_model=db["Cnn_model"].find({'creation':solution})

    #convert the model to json
    for i in new_model:
        json_data=i
    #select the model in the dictionary
    pickled_model=json_data['model']

    #return the model ready to be loaded
    return pickle.loads(pickled_model)
    