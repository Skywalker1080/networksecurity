import logging
import os
from datetime import datetime

#Log file syntax
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#Logfile path
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

#Complete log file path
LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

#logger config
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)