#from pymongo.mongo_client import MongoClient
import pymongo
import json
import pandas as pd
import os,sys
from schema import write_schema_yaml

# MongoDB connection URI
uri = "mongodb+srv://sasi:sasi123@cluster0.5st7jeq.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = r"/Users/shashidivya/Desktop/Ml_New_Mac/Mlops_Mac/Data/train.csv"
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ == "__main__":



    ROOT_DIR = os.getcwd()

    DATA_FILE_PATH = os.path.join(ROOT_DIR,'Data','train.csv')

    FILE_PATH = os.path.join(ROOT_DIR,DATA_FILE_PATH)

    write_schema_yaml(csv_file=FILE_PATH)


    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    # Convert the DataFrame to a list of dictionaries (JSON records)
    json_records = json.loads(df.to_json(orient="records"))
    print(json_records[0])

    # Establish a connection to MongoDB
    client = pymongo.MongoClient(uri)

    # Access the desired database and collection
    db = client[DATABASE]
    collection = db[COLLECTION_NAME]

    # Insert the JSON records into the collection
    collection.insert_many(json_records)

    # Close the MongoDB connection
    client.close()



