# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")


# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline
# import os
pipline = TrainPipeline()
pipline.run_pipeline()
# from src.constants import MONGODB_URL_KEY


# # print(os.getenv(MONGODB_URL_KEY).strip())
# import os

# print(repr(os.getenv("MONGODB_URL")))
# from src.entity.config_entity import DataValidationConfig
# from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
# class DataValidation:
#     def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
#         """
#         :param data_ingestion_artifact: Output reference of data ingestion artifact stage
#         :param data_validation_config: configuration for data validation
#         """
       
#         self.data_ingestion_artifact = data_ingestion_artifact
#         self.data_validation_config = data_validation_config

# data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
#                                              data_validation_config=self.data_validation_config

# from src.components.data_ingestion import DataIngestion
# from src.components.data_validation import DataValidation
# from src.components.data_transformation import DataTransformation
# # from src.components.model_trainer import ModelTrainer
# # from src.components.model_evaluation import ModelEvaluation
# # from src.components.model_pusher import ModelPusher

# from src.entity.config_entity import (DataIngestionConfig,
# #                                           DataValidationConfig,
#                                           DataTransformationConfig)

# from src.entity.artifact_entity import (DataIngestionArtifact,
#                                             DataValidationArtifact,
#                                             DataTransformationArtifact)

# print(DataIngestionArtifact.test_file_path)