from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        logging.info("data ingestion started")
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("initiated data ingestion")

        dataingestionartifact = data_ingestion.initiate_Data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)

