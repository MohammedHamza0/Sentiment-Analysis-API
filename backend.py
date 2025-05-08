from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from src.config import Settings, get_settings
from src.utils.inferance import TextClassifier
from src.schemas.input_output_schema import text_request, PredictionResponse



# Initialize the TextClassifier
text_classifier = TextClassifier(model_type="glove", model_name="svm")

# Intialize FastAPI app
app = FastAPI(title=get_settings().APP_NAME, 
              version=get_settings().VERSION,
              description="API Sentiment Analysis for twitter data")


# open cors (Cross-Origin Resource Sharing) for all origins
# This is important for the frontend to access the backend API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api_key_header = APIKeyHeader(name="X-API-Key")
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != get_settings().API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key



@app.get("/", tags=["Healthy"], description="Healthy check endpoint")
async def Home(settings: Settings = Depends(get_settings)):
     return {
          "app_name": settings.APP_NAME,
          "version": settings.VERSION,
          "message": "Welcome to the Sentiment Analysis API"
     }
     
     
@app.post("/predict", tags=["Predict"], description="Predict sentiment", response_model=PredictionResponse)
async def Predict(texts: text_request, api_key: str = Depends(verify_api_key)):
     try:
          predictions_raw = text_classifier.predict(texts.texts)
          # Map the keys to match the PredictionResponse schema
          predictions = [
               {"text": item["Text"], "sentiment": item["Sentiment"]}
               for item in predictions_raw
          ]
          return PredictionResponse(predictions=predictions)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))