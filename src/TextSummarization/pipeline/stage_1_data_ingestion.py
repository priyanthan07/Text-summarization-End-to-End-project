from src.TextSummarization.components.data_ingestion import DataIngestion
from src.TextSummarization.config.configuration import ConfigurationManager
from src.TextSummarization.logging.Logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()

            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config = data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            print(e)