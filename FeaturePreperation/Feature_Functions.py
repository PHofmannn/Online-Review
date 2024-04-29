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



# Function for Title Length (TL), sets 0 if the title is empty/consists of only a special character
def title_length(df):
    # Count the number of titles
    df['title_length'] = df['title_x'].apply(lambda x: len(x) if x.strip().isalnum() else 1)
    return df


# Function for calculating the Flesch-Kincaid readability score
def calculate_flesch_kincaid(df):
    # Import the Readability library
    from readability import Readability
    from readability.exceptions import ReadabilityException

    # Initialize an empty list to store readability scores
    readability_scores = []

    # Iterate through each text in the DataFrame
    for text in df['text']:
        try:
            # Calculate the Flesch-Kincaid score
            r = Readability(text)
            score = r.flesch_kincaid().score
        except ReadabilityException:
            # If the ReadabilityException occurs (due to less than 100 words), set score to NaN
            score = float('nan')
        
        # Append the score to the list of readability scores
        readability_scores.append(score)

    # Add the readability scores as a new column to the DataFrame
    df['F-K_score'] = readability_scores

    return df



# Function for calculating the review extremity score (Difference between avg Rating and Rating)
def calculate_review_extremity(df):
    # Calculate the review extremity as the difference between review rating and average product rating
    df['review_extremity'] = df['rating'] - df['average_rating']
    return df



# Calculate the elapsed time since the review was posted
def calculate_elapsed_time(df):
    # Convert timestamp column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Find the most recent timestamp
    recent_timestamp = df['timestamp'].max()
    
    # Calculate elapsed time for each review in days
    df['elapsed_time_days'] = (recent_timestamp - df['timestamp']).dt.days
    
    return df


# Function for checking whether the review contains images
def image_check(df):
    # Check if the value in the "images" column is an empty list
    df['image'] = df['images'].apply(lambda x: 0 if x == "[]" else 1)
    return df


def verified_pur(df):
    # Check if the value in the "verified_purchase" column is True or False
    df['VerPurch'] = df['verified_purchase'].apply(lambda x: 1 if x else 0)
    return df


# Function for updating timestamp information
def extract_timestamp(df):
    # Convert timestamp column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Extract year, month, and day from the timestamp
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['day'] = df['timestamp'].dt.day
    df['hour'] = df['timestamp'].dt.hour

    return df


# Function for verifying verified_purchase
def verified_purchase(df):
    # Check if the value in the "images" column is an empty list
    df['verified_pur'] = df['verified_purchase'].apply(lambda x: 0 if x == "false" else 1)
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
    df = image_check(df)
    df = verified_purchase(df)
    df = extract_timestamp(df)
    return df


