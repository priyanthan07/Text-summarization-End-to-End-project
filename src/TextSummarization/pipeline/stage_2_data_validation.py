from src.TextSummarization.components.data_validation import DataValidation
from src.TextSummarization.config.configuration import ConfigurationManager
from src.TextSummarization.logging.Logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()

            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_files_exist()

        except Exception as e:
            print(e)