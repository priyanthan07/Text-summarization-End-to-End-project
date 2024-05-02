from src.TextSummarization.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from src.TextSummarization.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
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
