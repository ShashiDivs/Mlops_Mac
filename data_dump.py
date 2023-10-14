from pymongo.mongo_client import MongoClient
import pymongo
import json
import pandas as pd

client = "mongodb+srv://shashi:sasidb09@cluster0.36yyeo2.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = "/Users/shashidivya/Desktop/aug_train.csv"
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)

    print(f"Rows and columns of our Data : {df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())

    print(json_record[0])

    client[DATABASE][COLLECTION_NAME].insert_many(json_record)