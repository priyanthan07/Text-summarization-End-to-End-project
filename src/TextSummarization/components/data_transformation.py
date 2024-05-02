import os
from src.TextSummarization.logging.Logging import logger
from src.TextSummarization.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        try:
            input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

            with self.tokenizer.as_target_tokenizer():
                target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

            return {
                'input_ids' : input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
                'labels': target_encodings['input_ids']
            }

        except Exception as e:
            logger.error(e)
            raise e
        
    def convert(self):
        logger.info("Converting examples to features")
        dataset = load_from_disk(self.config.data_path)
        dataset_conv= dataset.map(self.convert_examples_to_features, batched = True)
        dataset_conv.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))
        logger.info("Finished converting examples to features")