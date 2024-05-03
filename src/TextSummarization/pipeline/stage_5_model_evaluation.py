from src.TextSummarization.components.model_evaluation import ModelEvaluation
from src.TextSummarization.config.configuration import ConfigurationManager
from src.TextSummarization.logging.Logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def evaluate(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config = model_evaluation_config)
            model_evaluation_config.evaluation()

        except Exception as e:
            print(e)