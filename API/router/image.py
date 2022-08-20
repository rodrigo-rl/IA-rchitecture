from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import APIRouter
from bson import json_util
from json import loads
import os

router=APIRouter()

load_dotenv()
client=MongoClient(os.getenv("URL"))
db=client.get_database("Data")

@router.get("/name/{name}")
def get_picture(name):
    res=list(db["Styles"].find({"Name":name}))
    aux=loads(json_util.dumps(res))

    return aux[0]['Pictures']#image['Pictures']
