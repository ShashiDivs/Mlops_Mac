import os,sys
from src.exception import CustomException
from src.logger import logging
from datetime import datetime
from src.constant import *
from src.utils import read_yaml_file

config_data = read_yaml_file(CONFIG_FILE_PATH)


class TrainingPipelineCinfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%m%S')}")
        except Exception as e:
            raise CustomException(e,sys)
        

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineCinfig):
        
        try:
            data_ingestion_key = config_data[DATA_INGESTION_CONFIG_KEY]
            
            self.datbase_name = data_ingestion_key[DATA_INGESTION_DATABASE_NAME]
            self.collection_name = data_ingestion_key[DATA_INGESTION_COLLECTION_NAME]


            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,data_ingestion_key)
            self.raw_data_dir = os.path.join(self.data_ingestion_dir,data_ingestion_key[DATA_INGESTION_RAW_DATA_DIR_KEY])
            self.ingested_data_dir = os.path.join(self.raw_data_dir,data_ingestion_key[DATA_INGESTION_INGESTED_DIR_KEY])
            self.train_file_path = os.path.join(self.ingested_data_dir,data_ingestion_key[DATA_INGESTION_INGESTED_TRAIN_DIR_KEY])
            self.test_file_path = os.path.join(self.ingested_data_dir,data_ingestion_key[DATA_INGESTION_INGESTED_TEST_DIR_KEY])
            
            self.test_size = 0.2


        except Exception as e:
            raise CustomException(e,sys)
        
