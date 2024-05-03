from fastapi import FastAPI
import os
import sys
import uvicorn
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.TextSummarization.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful...")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    

    
@app.post("/predict")
async def prediction(text):
    try:        
        pipeline = PredictionPipeline()
        summary = pipeline.predict(text)
        return summary
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)