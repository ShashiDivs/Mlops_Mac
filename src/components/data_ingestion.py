
import os,sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.config import *
from src.constant import *
from src.entity.config_enitity import DataIngestionConfig
from src.utils import read_yaml_file,get_collection_as_dataframe
import numpy as np


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging("*********************Data Ingestion Started*************************")
            self.ddata_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
        


    def get_data_from_mongo(self):
        df : pd.DataFrame = get_collection_as_dataframe(
            database_name=self.data_ingestion_config,
            collection_name=self.ddata_ingestion_config.collection_name
        )