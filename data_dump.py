#from pymongo.mongo_client import MongoClient
import pymongo
import json
import pandas as pd

# MongoDB connection URI
uri = "mongodb+srv://sasi:sasi123@cluster0.5st7jeq.mongodb.net/?retryWrites=true&w=majority"

DATA_FILE_PATH = r"/Users/shashidivya/Desktop/Ml_New_Mac/Mlops_Mac/Data/train.csv"
DATABASE = "Machine_learning"
COLLECTION_NAME = "DATASET"

if __name__ == "__main__":
    # Read data from the CSV file into a Pandas DataFrame
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