from src.TextSummarization.components.model_trainer import ModelTrainer
from src.TextSummarization.config.configuration import ConfigurationManager
from src.TextSummarization.logging.Logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def train(self):
        try:
            config = ConfigurationManager()
            model_training_config = config.get_model_training_config()
            model_training_config = ModelTrainer(config=model_training_config)
            model_training_config.train()

        except Exception as e:
            print(e)