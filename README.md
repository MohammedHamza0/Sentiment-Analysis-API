# Sentiment-Analysis-API

## Overview
This project is a Sentiment Analysis API designed to process text data and classify sentiments using various machine learning models. It includes components for text preprocessing, model artifacts, and datasets for training and testing. The project provides both a backend API and a Streamlit-based frontend for user interaction.

## Project Structure

```
Sentiment-Analysis-API/
├── backend.py                # Backend logic for the API
├── frontend.py               # Streamlit frontend for the API
├── template.py               # Template for creating new components
├── LICENSE                   # License information
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── artifacts/                # Pre-trained model artifacts
│   ├── bow.pkl
│   ├── glove.pkl
│   ├── svm_model_bow.pkl
│   ├── svm_model_glove.pkl
│   ├── svm_model_tfidf.pkl
│   ├── tf-idf.pkl
│   ├── rf_model_bow.pkl
│   ├── rf_model_glove.pkl
│   └── rf_model_tfidf.pkl
├── DataSets/                 # Datasets for training and testing
│   └── testdata.manual.2009.06.14.csv
├── images/                   # Images used in the project
│   └── Blog_DA_Sentiment_Customer_08052022.png
├── NoteBooks/                # Jupyter notebooks for experimentation
│   └── notebook.ipynb
├── src/                      # Source code for the project
│   ├── __init__.py
│   ├── config.py             # Configuration settings
│   ├── schemas/              # Input and output schemas
│   │   ├── __init__.py
│   │   └── input_output_schema.py
│   └── utils/                # Utility functions and classes
│       ├── __init__.py
│       ├── inferance.py      # Inference logic for sentiment analysis
│       └── text_processor.py # Text preprocessing logic
```

## Key Components

### Backend and Frontend
- **backend.py**: Contains the backend logic for handling API requests. It uses FastAPI to expose endpoints for sentiment analysis.
- **frontend.py**: Provides a Streamlit-based user interface for interacting with the API. It allows users to input text, select models, and view sentiment predictions.

### Template
- **template.py**: A template file for creating new components or modules in the project. This file provides a structured starting point for adding new functionality.

### Artifacts
- Pre-trained models and vectorizers stored in the `artifacts/` directory. These include:
  - **bow.pkl**: Bag of Words vectorizer.
  - **glove.pkl**: GloVe embeddings.
  - **tf-idf.pkl**: TF-IDF vectorizer.
  - **svm_model_bow.pkl**, **svm_model_glove.pkl**, **svm_model_tfidf.pkl**: SVM models for different vectorization techniques.
  - **rf_model_bow.pkl**, **rf_model_glove.pkl**, **rf_model_tfidf.pkl**: Random Forest models for different vectorization techniques.

### Datasets
- The `DataSets/` folder contains datasets for testing and evaluation, such as `testdata.manual.2009.06.14.csv`.

### Images
- The `images/` folder contains images used in the project, such as for the frontend UI.

### Notebooks
- The `NoteBooks/` folder includes Jupyter notebooks for data exploration, experimentation, and model training.

### Source Code
- The `src/` directory contains the main source code, including configuration, schemas, and utility functions for text processing and inference.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MohammedHamza0/Sentiment-Analysis-API.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Sentiment-Analysis-API
   ```
3. Create a new Python environment (Python 3.10):
   ```bash
   python -m venv venv
   ```
4. Activate the environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Project**:
   - The frontend will automatically start the backend when you run it. Simply execute:
     ```bash
     streamlit run frontend.py
     ```
   - This will start the Streamlit frontend and the backend server.

2. **Access the Frontend**:
   - Open your browser and navigate to:
     ```
     http://localhost:8501
     ```

3. **Input Text and Analyze Sentiment**:
   - Enter text for sentiment analysis in the provided text area.
   - Select the model type (e.g., TF-IDF, BoW, GloVe) and model name (e.g., SVM, RF) from the sidebar.
   - Click the "Analyze Sentiment" button to view the predictions.

## API Endpoints

### `/predict`
- **Method**: `POST`
- **Description**: Predicts the sentiment of the input text.
- **Request Body**:
  ```json
  {
    "texts": ["Sample text 1", "Sample text 2"],
    "model_type": "tfidf",
    "model_name": "svm"
  }
  ```
- **Headers**:
  - `X-API-Key`: Your API key for authentication.
- **Response**:
  ```json
  {
    "predictions": [
      {"text": "Sample text 1", "sentiment": "Positive"},
      {"text": "Sample text 2", "sentiment": "Negative"}
    ]
  }
  ```

## Troubleshooting

1. **Backend Connection Issues**:
   - Ensure no other process is using port `8000`.
   - Manually start the backend using:
     ```bash
     uvicorn backend:app --host 127.0.0.1 --port 8000 --reload
     ```

2. **Dependencies**:
   - Ensure all dependencies are installed using:
     ```bash
     pip install -r requirements.txt
     ```

3. **API Key**:
   - Ensure you provide a valid API key in the frontend sidebar.

## License
This project is licensed under the terms specified in the `LICENSE` file.