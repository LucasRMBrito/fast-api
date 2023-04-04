from pymongo import MongoClient


client = MongoClient("mongodb+srv://luquinharoger:123123123@cluster0.mllhdgg.mongodb.net/?retryWrites=true&w=majority")

db = client.test

colecao = db["testando"]