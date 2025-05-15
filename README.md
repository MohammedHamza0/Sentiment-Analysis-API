# Sentiment-Analysis-API

## Team Members
* Mohammed Hamza Moawad  (412200058)
* Abdelrahman Ahmed Eldaba (412200228)
* Ahmed Mohamed Esmail  (412200120)
* Hoda Mohamed Elwakeel  (412200403)
* Al-Zahra Ali Eissa  (412200010)
* Aseel Samy Ahmed Al-Faqih  (412200430)

## Overview
This project is a Sentiment Analysis API designed to process text data and classify sentiments using various machine learning models. It includes components for text preprocessing, model artifacts, and datasets for training and testing. The project provides both a backend API and a Streamlit-based frontend for user interaction.

## Project Structure

```
Sentiment-Analysis-API/
├── src/                      # Source code for the project
│   ├── __init__.py          # Package initialization
│   ├── Controller/          # API controllers and routes
│   │   ├── __init__.py
│   │   ├── app_router.py    # Main API routes
│   │   └── base_router.py   # Base router configuration
│   ├── Model/               # Data models and ML components
│   │   ├── __init__.py
│   │   └── input_output_schema.py
│   ├── View/                # Frontend components
│   │   ├── __init__.py
│   │   └── frontend.py      # Streamlit UI
│   ├── Utils/               # Utility functions
│   │   ├── __init__.py
│   │   └── config.py        # Configuration settings
│   └── Core/                # Core application components
│       ├── __init__.py
│       └── backend.py       # FastAPI application
├── Artifacts/               # Pre-trained model artifacts
│   ├── bow.pkl
│   ├── glove.pkl
│   ├── svm_model_bow.pkl
│   ├── svm_model_glove.pkl
│   ├── svm_model_tfidf.pkl
│   ├── tf-idf.pkl
│   ├── rf_model_bow.pkl
│   ├── rf_model_glove.pkl
│   └── rf_model_tfidf.pkl
├── DataSets/                # Datasets for training and testing
│   └── testdata.manual.2009.06.14.csv
├── images/                  # Images used in the project
│   └── Blog_DA_Sentiment_Customer_08052022.png
├── NoteBooks/               # Jupyter notebooks for experimentation
│   └── notebook.ipynb
├── setup.py                 # Package installation configuration
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── LICENSE                  # License information
└── README.md               # Project documentation
```

## Key Components

### MVC Architecture
- **Model**: Contains data models, schemas, and ML components
- **View**: Contains the Streamlit-based frontend interface
- **Controller**: Contains API routes and request handlers
- **Utils**: Contains configuration and utility functions
- **Core**: Contains the main FastAPI application

### Artifacts
Pre-trained models and vectorizers stored in the `Artifacts/` directory:
- **bow.pkl**: Bag of Words vectorizer
- **glove.pkl**: GloVe embeddings
- **tf-idf.pkl**: TF-IDF vectorizer
- **svm_model_*.pkl**: SVM models for different vectorization techniques
- **rf_model_*.pkl**: Random Forest models for different vectorization techniques

### Datasets
The `DataSets/` folder contains datasets for testing and evaluation.

### Images
The `images/` folder contains images used in the project UI.

### Notebooks
The `NoteBooks/` folder includes Jupyter notebooks for data exploration and model training.

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

5. Install the package in development mode:
   ```bash
   pip install -e .
   ```

6. Create a `.env` file in the root directory:
   ```
   API_SECRET_KEY=your-secret-key-here
   ```

## Usage

1. **Run the Project**:
   ```bash
   python run.py
   ```
   This will start both the Streamlit frontend and the FastAPI backend.

2. **Access the Frontend**:
   Open your browser and navigate to:
   ```
   http://localhost:8501
   ```

3. **Input Text and Analyze Sentiment**:
   - Enter text for sentiment analysis in the provided text area
   - Select the model type (TF-IDF, BoW, GloVe) and model name (SVM, RF) from the sidebar
   - Enter your API key in the sidebar
   - Click the "Analyze Sentiment" button to view the predictions

## API Endpoints

### `/predict`
- **Method**: `POST`
- **Description**: Predicts the sentiment of the input text
- **Request Body**:
  ```json
  {
    "texts": ["Sample text 1", "Sample text 2"],
    "model_type": "tfidf",
    "model_name": "svm"
  }
  ```
- **Headers**:
  - `X-API-Key`: Your API key for authentication
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

1. **Import Issues**:
   - If you encounter import errors, make sure you've installed the package in development mode:
     ```bash
     pip install -e .
     ```

2. **Backend Connection Issues**:
   - The frontend will automatically start the backend
   - Default backend runs on `http://127.0.0.1:5000`
   - Check if the port is already in use

3. **API Key**:
   - Ensure you've created a `.env` file with your API key
   - Make sure to enter the same API key in the frontend sidebar

## License
This project is licensed under the terms specified in the `LICENSE` file.
