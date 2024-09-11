import boto3
import pandas as pd

df = pd.read_csv("reviews.csv")


# Initialize a boto3 client for Amazon Comprehend
comprehend = boto3.client('comprehend', region_name='ap-south-1')

# Example list of reviews
reviews = df["Description"]
# Loop through each review and analyze its sentiment
for review in reviews:
    response = comprehend.detect_sentiment(Text=review, LanguageCode='en')
    print(f"Review: {review}")
    print(f"Sentiment: {response['Sentiment']}")
    print(f"Confidence Scores: {response['SentimentScore']}\n")


print(df["Description"])