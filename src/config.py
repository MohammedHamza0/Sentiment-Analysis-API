import os
from dotenv import load_dotenv
load_dotenv(override=True)
import joblib


# Load dot env variables
APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")




# Create variable to access the artifacts dir
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACTS_DIR = os.path.join(PROJECT_DIR, "artifacts")


# Load models & vectorizers
tfidf_vectorizer = joblib.load(os.path.join(ARTIFACTS_DIR, "tf-idf.pkl"))
bow_vectorizer = joblib.load(os.path.join(ARTIFACTS_DIR, "bow.pkl"))
svm_ifidf_model = joblib.load(os.path.join(ARTIFACTS_DIR, "svm_model_tfidf.pkl"))
svm_bow_model = joblib.load(os.path.join(ARTIFACTS_DIR, "svm_model_bow.pkl"))




EMOTIONS_DICT = {
    # 🙂 Emojis
    "😀": "grinning face",
    "😁": "beaming face with smiling eyes",
    "😂": "face with tears of joy",
    "🤣": "rolling on the floor laughing",
    "😃": "grinning face with big eyes",
    "😄": "grinning face with smiling eyes",
    "😅": "grinning face with sweat",
    "😉": "winking face",
    "😊": "smiling face with smiling eyes",
    "😍": "smiling face with heart eyes",
    "😘": "face blowing a kiss",
    "😎": "smiling face with sunglasses",
    "🥰": "smiling face with hearts",
    "😒": "unamused face",
    "😭": "loudly crying face",
    "😢": "crying face",
    "😡": "angry face",
    "😠": "angry face",
    "🤬": "face with symbols on mouth",
    "😩": "weary face",
    "😤": "face with steam from nose",
    "🤯": "exploding head",
    "😱": "screaming in fear",
    "👍": "thumbs up",
    "👎": "thumbs down",
    "❤️": "love",
    "💔": "broken heart",
    "🔥": "fire",
    "💯": "hundred points",
    "🙏": "folded hands",

    # 🙂 Emoticons
    ":)": "smiley face",
    ":-)": "smiley face",
    ":D": "grinning face",
    ":-D": "grinning face",
    ":(": "sad face",
    ":-(": "sad face",
    ":/": "unsure face",
    ":-/": "unsure face",
    ":|": "neutral face",
    ":-|": "neutral face",
    ":'(": "crying face",
    ":'-)": "crying face",
    ":P": "playful face",
    ":-P": "playful face",
    ";)": "winking face",
    ";-)": "winking face",
    ">:(": "angry face",
    "<3": "love",
    "</3": "broken heart"
}



NEGATION_STOPWORDS = {
    "no", "not", "nor", "never", "n't", "cannot",
    "don't", "doesn't", "didn't", "won't", "wouldn't",
    "shouldn't", "can't", "couldn't", "isn't", "aren't", "wasn't", "weren't", "nothing", "nowhere", "neither", "nobody", "none"
}

