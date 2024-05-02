from src.TextSummarization.components.data_transformation import DataTransformation
from src.TextSummarization.config.configuration import ConfigurationManager
from src.TextSummarization.logging.Logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()

            data_validation_config = config.get_data_transformation_config()
            data_validation = DataTransformation(config = data_validation_config)
            data_validation.convert()

        except Exception as e:
            print(e)