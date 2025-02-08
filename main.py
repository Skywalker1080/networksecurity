from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
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
        logging.info("data ingestion completed")
        print(dataingestionartifact)

        
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("initiated data validation")
        data_validation_artifiact = data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifiact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)

