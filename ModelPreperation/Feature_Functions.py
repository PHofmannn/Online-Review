import spacy
import pandas as pd
from readability import Readability
import nltk
import re
nltk.download('punkt')



# Function for calculating the helfpul ratio (HR) of a review
def calculate_helpful_ratio(df):
    # Calculate the total number of helpful votes across all reviews
    total_helpful_votes = df['helpful_vote'].sum()
    
    # Calculate the ratio of helpful votes for each review relative to the total
    df['helpful_ratio'] = df['helpful_vote'] / total_helpful_votes
    
    return df


# Load spaCy English model and prepare function to get the POS tags  for counting adverbs, adjectives and nouns
nlp = spacy.load("en_core_web_sm")

def count_pos_tags(df):
    # Load spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Define a function to count POS tags in the text
    def count_pos_tags(text):
        # Process the text with spaCy
        doc = nlp(text)
        
        # Initialize counts
        noun_count = 0
        adj_count = 0
        adv_count = 0
        
        # Iterate through tokens and count POS tags
        for token in doc:
            if token.pos_ == "NOUN":
                noun_count += 1
            elif token.pos_ == "ADJ":
                adj_count += 1
            elif token.pos_ == "ADV":
                adv_count += 1
        
        return noun_count, adj_count, adv_count

    # Apply the function to the 'text' column to calculate POS tag counts
    df[['noun_count', 'adj_count', 'adv_count']] = df['text'].apply(lambda x: pd.Series(count_pos_tags(x)))

    return df


# Function for counting the number of words in a text
def word_count(df):
    # Define a function to count the number of words in a text
    def count_words(text):
        # Split the text into words
        words = text.split()
        return len(words)

    # Apply the function to the 'text' column to calculate word counts
    df['word_count'] = df['text'].apply(count_words)
    return df



# Function for counting the number of sentences in a review
def sentence_count(df):
    def count_sentences(text):
        # Ensure each sentence ends with '.', '?', or '!'
        text = str(text).strip()  # Convert to string and remove leading/trailing whitespace
        if not re.search(r'[.!?]$', text):
            text += '.'  # Add a period at the end if missing

        sentences = nltk.sent_tokenize(text)
        return len(sentences)

    df['sentence_count'] = df['text'].apply(count_sentences)
    return df


# Function for counting the average number of words per sentence
def average_words_per_sentence(df):
    def calculate_avg_words_per_sentence(text, num_sentences):
        # Tokenize the text into words
        words = nltk.word_tokenize(text)
        
        # Calculate the total number of words
        total_words = len(words)
        
        # Calculate the average words per sentence
        if num_sentences == 0:
            return 0
        else:
            return total_words / num_sentences

    # Apply the function to the 'text' column to calculate average words per sentence
    df['avg_words_per_sentence'] = df.apply(lambda row: calculate_avg_words_per_sentence(row['text'], row['sentence_count']), axis=1)
    return df



# Function for Title Length (TL)
def title_length(df):
    # Count the number of titles
    df['title_length'] = df['title_x'].apply(lambda x: len(x))
    return df



def calculate_flesch_kincaid(df):
    # Initialize Readability object with the text
    readability_scores = []

    for text in df['text']:
        # Check if the text contains at least 100 words
        if len(text.split()) >= 100:
            r = Readability(text)
            # Calculate the Flesch-Kincaid score
            score = r.flesch_kincaid().score
            readability_scores.append(score)
        else:
            # If the text has fewer than 100 words, append NaN
            readability_scores.append(float('nan'))

    # Add the Flesch-Kincaid score as a new column to the DataFrame
    df['F–K_score'] = readability_scores
    return df


# Function for calculating the review extremity score (Difference between avg Rating and Rating)
def calculate_review_extremity(df):
    # Calculate the review extremity as the difference between review rating and average product rating
    df['review_extremity'] = df['rating'] - df['average_rating']
    return df



# Caöculate the elapsed time since the review was posted
def calculate_elapsed_time(df):
    # Convert timestamp column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Find the most recent timestamp
    recent_timestamp = df['timestamp'].max()
    
    # Calculate elapsed time for each review in days
    df['elapsed_time_days'] = (recent_timestamp - df['timestamp']).dt.days
    
    return df



## Applying all functions to the dataframe

def feature_building(df):
    # Apply all individual functions to the DataFrame
    df = calculate_helpful_ratio(df)
    df = count_pos_tags(df)
    df = word_count(df)
    df = sentence_count(df)
    df = average_words_per_sentence(df)
    df = title_length(df)
    df = calculate_flesch_kincaid(df)
    df = calculate_review_extremity(df)
    df = calculate_elapsed_time(df)

    return df
