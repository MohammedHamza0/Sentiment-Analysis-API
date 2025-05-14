from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.config import Settings, get_settings
from src.routers import APP_ROUTER, BASE_ROUTER




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


# Include the routers
app.include_router(APP_ROUTER)
app.include_router(BASE_ROUTER)

