from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import APIRouter
from bson import json_util
from json import loads
import os
import random

router=APIRouter()

load_dotenv()
client=MongoClient(os.getenv("URL"))
db=client.get_database("Data")

@router.get("/school/{school}")
def get_styles(school):
    random_list = []
    li=range(1,10)
    #we use this list to get non-repeating elemets
    random_list=random.sample(li,3)

    res=list(db["Styles"].find({"School":school}))

    solution=[]
    for i in range(len(res)):
        if i in random_list:
            solution.append(loads(json_util.dumps(res[i])))

    return solution
