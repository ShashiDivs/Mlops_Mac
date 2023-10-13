import logging
import os,sys
from datetime import datetime



LOGIN_DIR = "logs"

LOGIN_DIR = os.path.join(os.getcwd(),LOGIN_DIR)

os.makedirs(LOGIN_DIR,exist_ok=True)


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOGIN_DIR,file_name)

logging.basicConfig(filename = log_file_path,
                    filemode='w',
                    format= '%(asctime)s %(name)s %(levelname)s %(message)s',
                    level = logging.INFO)