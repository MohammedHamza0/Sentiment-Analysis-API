from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from src.config import (APP_NAME, VERSION, API_SECRET_KEY, svm_bow_model, 
                     svm_ifidf_model, tfidf_vectorizer, bow_vectorizer)
from src.utils.inferance import TextClassifier
from src.schemas.input_output_schema import text_request, PredictionResponse



# Initialize the TextClassifier
text_classifier = TextClassifier(model_type="tfidf")

# Intialize FastAPI app
app = FastAPI(title=APP_NAME, 
              version=VERSION,
              description="API Sentiment Analysis for twitter data")


# open cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api_key_header = APIKeyHeader(name="X-API-Key")
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key



@app.get("/", tags=["Healthy"], description="Healthy check endpoint")
async def Home():
     return {
          "app_name": APP_NAME,
          "version": VERSION,
          "message": "Welcome to the Sentiment Analysis API"
     }
     
     
@app.post("/predict", tags=["Predict"], description="Predict sentiment")
async def Predict(texts: text_request, api_key: str = Depends(verify_api_key)):
     try:
          predictions = text_classifier.predict(texts.texts)
          return PredictionResponse(predictions=predictions)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))