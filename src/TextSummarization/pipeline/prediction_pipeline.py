from src.TextSummarization.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = self.config.model_path

        kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        Pipeline = pipeline("summarization", model= model, tokenizer=tokenizer)

        print("Dialog:")
        print(text)

        summary = Pipeline(text, **kwargs)[0]["summary_text"]

        print("\nModel Summary:")
        print(summary)

        return summary

