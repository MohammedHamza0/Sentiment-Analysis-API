from typing import List, Dict

from .text_processor import TextProcessor
from src.config import (tfidf_vectorizer, 
                        bow_vectorizer)


from src.config import CLASS_MAPS


class TextClassifier:
     def __init__(self, model_type: str = "tfidf"):
          self.processor = TextProcessor()
          self.class_maps = CLASS_MAPS
          self.model = None
          self.vectorizer = None
          if model_type == "tfidf":
               self.model = svm_ifidf_model
               self.vectorizer = tfidf_vectorizer
          elif model_type == "bow":
               self.model = svm_bow_model
               self.vectorizer = bow_vectorizer
          else:     
               raise ValueError("Invalid model type. Choose 'tfidf' or 'bow'.")
          
          
     def predict(self, texts: List[str]) -> List[Dict[str, str]]:
          # Text Preprocessing
          proccessed_texts = [self.processor.process_text(text) for text in texts]
          
          # Vectorization
          vectorized_texts = self.vectorizer.transform(proccessed_texts).toarray()
          
          # prediction
          raw_predictions = self.model.predict(vectorized_texts)
          
          predictions = []
          
          for text, pred in zip(texts, raw_predictions):
               pred_label = self.class_maps.get(int(pred), "Unknown")
               predictions.append({"Text": text, "Sentiment": pred_label})
               
          return predictions
          
          
     
          
          