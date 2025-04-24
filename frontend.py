import streamlit as st
import requests
import os
import subprocess

# Streamlit app title
st.title("Sentiment Analysis API Frontend")

# Add an image under the title
# st.image("images/Blog_DA_Sentiment_Customer_08052022.png", use_column_width=True)

# Ensure the backend is running
backend_process = None
if not os.system("tasklist | findstr uvicorn"):
    st.info("Backend is already running.")
else:
    try:
        backend_process = subprocess.Popen(
            ["uvicorn", "backend:app", "--host", "127.0.0.1", "--port", "8000"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        st.success("Backend started successfully.")
    except Exception as e:
        st.error(f"Failed to start the backend: {e}")

input_text = st.text_area("Enter text for sentiment analysis:")

with st.sidebar:
     st.image("images/Blog_DA_Sentiment_Customer_08052022.png", use_column_width=True)
     st.header("API Key")
     API_KEY = st.text_input("Enter your API Key", type="password")
     st.markdown("**Note:** This API key is used to authenticate your requests.")
     
if st.button("Analyze Sentiment"):
     with st.spinner("Analyzing..."):
          if input_text.strip():
               try:
                    sentences = [s.strip() for s in input_text.split("\n") if s.strip()]

                    # Send request to the backend API with the API key in headers
                    response = requests.post(
                         "http://127.0.0.1:8000/predict",
                         json={"texts": sentences},
                         headers={"X-API-Key": API_KEY}
                    )

                    # Handle response
                    if response.status_code == 200:
                         result = response.json()
                         predictions = result.get("predictions", [])
                         if predictions:
                              for prediction in predictions:
                                   if prediction['sentiment'] == "Negative":
                                        st.success(f"'💬Text': {prediction['text']}\n >>>> '✅Sentiment': {prediction['sentiment']} 😢")
                                   elif prediction['sentiment'] == "Positive":
                                        st.success(f"'💬Text': {prediction['text']}\n >>>> '✅Sentiment': {prediction['sentiment']} 😊")
                                   else:
                                        st.success(f"'💬Text': {prediction['text']}\n >>>> '✅Sentiment': {prediction['sentiment']} 😐")

                         else:    
                              st.warning("No predictions returned from the API.")
                    else:
                         st.error(f"Error: {response.status_code} - {response.text}")
               except Exception as e:
                    st.error(f"An error occurred: {e}")
          else:
               st.warning("Please enter some text for analysis.")