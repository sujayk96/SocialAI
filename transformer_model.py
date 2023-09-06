import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import pandas as pd

# Load the pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Define a list of depression-related keywords
depression_keywords = ["depressed", "sad", "hopeless", "lonely", "worthless", "suicidal", "anxious"]

# Function to detect depression indicators using BERT
def detect_depression(text):
    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    # Get the model's output
    outputs = model(**inputs)
    logits = outputs.logits

    # Calculate probabilities using softmax
    probabilities = softmax(logits, dim=1)[0]

    # Check if any depression keywords are present in the text
    depression_score = sum(1 for word in text.lower().split() if word in depression_keywords)

    return probabilities[1].item(), outputs

def get_sentiment_scores(input_text):
    depression_probability, outputs = detect_depression(input_text)
    print("depression_probability", depression_probability, outputs)
    return depression_probability

def generate_op(file_name):
    df = pd.read_csv(file_name)
    df['Score'] = df['Text'].astype(str).apply(get_sentiment_scores)
    df.to_csv(file_name)
    return
