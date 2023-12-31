import os,sys
from src.exception import CustomException
from src.logger import logger
from datetime import datetime
from src.constant import *
import yaml
import pandas as pd
from src.data_access import mongodb_client



def read_yaml_file(filepath:str)->dict:
    try:
        with open(filepath,"r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e,sys)
        
# database -> json -> convert into Dataframe
def get_collection_as_dataframe(datbase_name:str,collection_name:str)->pd.DataFrame:
    try:
        client = mongodb_client()
        df = pd.DataFrame(list(client[datbase_name][collection_name].find()))

        if "_id" in df.columns:
            df = df.drop("_id",axis=1)
        return df
    except Exception as e:
        raise CustomException(e,sys) from e
