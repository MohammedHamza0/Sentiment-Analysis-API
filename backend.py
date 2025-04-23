from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.config import (APP_NAME, VERSION, API_SECRET_KEY, svm_bow_model, 
                     svm_ifidf_model, tfidf_vectorizer, bow_vectorizer)




# Intialize FastAPI app
app = FastAPI(title=APP_NAME, 
              version=VERSION,
              description="API Sentiment Analysis for twitter data")


@app.get("/", tags=["Healthy"], description="Healthy check endpoint")
async def Home():
     return {
          "app_name": APP_NAME,
          "version": VERSION,
          "message": "Welcome to the Sentiment Analysis API"
     }
     