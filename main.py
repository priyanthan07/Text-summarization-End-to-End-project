from src.TextSummarization.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from src.TextSummarization.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from src.TextSummarization.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
from src.TextSummarization.pipeline.stage_4_model_training import ModelTrainingPipeline
from src.TextSummarization.pipeline.stage_5_model_evaluation import ModelEvaluationPipeline
from src.TextSummarization.logging.Logging import logger

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>> stated {STAGE_NAME}<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> completed {STAGE_NAME}<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation stage'

try:
    logger.info(f">>>> stated {STAGE_NAME}<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> completed {STAGE_NAME}<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation stage'

try:
    logger.info(f">>>> stated {STAGE_NAME}<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> completed {STAGE_NAME}<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training stage'

try:
    logger.info(f">>>> stated {STAGE_NAME}<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.train()
    logger.info(f">>>> completed {STAGE_NAME}<<<<")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evaluation stage'

try:
    logger.info(f">>>> stated {STAGE_NAME}<<<<")
    model_trainer = ModelEvaluationPipeline()
    model_trainer.evaluate()
    logger.info(f">>>> completed {STAGE_NAME}<<<<")

except Exception as e:
    logger.exception(e)
    raise e