from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "mongodb+srv://bayosol372:RodBrx8EjbcXTUaR@cluster0.mnuki.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to client
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME = 'Aagam'
COLLECTION_NAME = 'waferfault'

df = pd.read_csv(r"C:\Users\Aagam Shah\Downloads\SensorProject\notebooks\wafer_23012020_041211.csv")

df=df.drop('Unnamed: 0', axis=1)

# Converting dataset into the list and uploading in the form of json
json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)