# Sentiment-Analysis-API

## Overview
This project is a Sentiment Analysis API designed to process text data and classify sentiments using various machine learning models. It includes components for text preprocessing, model artifacts, and datasets for training and testing.

## Project Structure

```
Sentiment-Analysis-API/
├── backend.py                # Backend logic for the API
├── frontend.py               # Streamlit frontend for the API
├── LICENSE                   # License information
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── artifacts/                # Pre-trained model artifacts
│   ├── bow.pkl
│   ├── svm_model_bow.pkl
│   ├── svm_model_glove.pkl
│   ├── svm_model_tfidf.pkl
│   ├── tf-idf.pkl
│   └── word2vec.model
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
- **backend.py**: Contains the backend logic for handling API requests.
- **frontend.py**: Provides a Streamlit-based user interface for interacting with the API.

### Artifacts
- Pre-trained models and vectorizers stored in the `artifacts/` directory.

### Datasets
- The `DataSets/` folder contains datasets for testing and evaluation.

### Images
- The `images/` folder contains images used in the project, such as for the frontend UI.

### Notebooks
- The `NoteBooks/` folder includes Jupyter notebooks for data exploration and experimentation.

### Source Code
- The `src/` directory contains the main source code, including configuration, schemas, and utility functions for text processing.

## Installation
1. Clone the repository:
   ```bash
   git clone <https://github.com/MohammedHamza0/Sentiment-Analysis-API.git>
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
1. Start the backend server:
   ```bash
   uvicorn backend:app --host 127.0.0.1 --port 8000
   ```
2. Run the Streamlit frontend:
   ```bash
   streamlit run frontend.py
   ```
3. Access the frontend interface in your browser at `http://localhost:8501`.

## License
This project is licensed under the terms specified in the `LICENSE` file.