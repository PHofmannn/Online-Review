import spacy
import pandas as pd
from readability import Readability
import nltk
import re
import textstat
nltk.download('punkt')

# Function for calculating the helpful ratio
def calculate_total_helpful_votes(df):
    for product_id, group in df.groupby('product'):
        total_helpful_votes = group['helpful_vote'].sum()
        df.loc[group.index, 'total_helpful_votes'] = total_helpful_votes
        df.loc[group.index, 'helpful_ratio'] = group['helpful_vote'] / total_helpful_votes

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
    df['WordC'] = df['text'].apply(count_words)
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

    df['SentC'] = df['text'].apply(count_sentences)
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
    df['SentL'] = df.apply(lambda row: calculate_avg_words_per_sentence(row['text'], row['SentC']), axis=1)
    return df



# Function for Title Length (TL), sets 0 if the title is empty/consists of only a special character
def title_length(df):
    # Count the number of titles
    df['TitleL'] = df['title_x'].apply(lambda x: len(x) if x.strip().isalnum() else 1)
    return df


# Function for calculating the Flesch Reading Ease score
def calculate_flesch_reading_score(df):
    # Initialize an empty list to store readability scores
    readability_scores = []

    # Iterate through each text in the DataFrame
    for text in df['text']:
        try:
            # Calculate the Flesch Reading Ease score using textstat
            score = textstat.flesch_reading_ease(text)
        except Exception as e:
            # If any exception occurs, set score to NaN
            score = float('nan')
        
        # Append the score to the list of readability scores
        readability_scores.append(score)

    # Add the readability scores as a new column to the DataFrame
    df['FRE'] = readability_scores

    return df



# Function for calculating the review extremity score (Difference between avg Rating and Rating)
def calculate_review_extremity(df):
    # Calculate the review extremity as the difference between review rating and average product rating
    df['RewExt'] = df['Rating'] - df['average_rating']
    return df



def calculate_elapsed_time(df):
    # Convert timestamp column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Group by product and calculate elapsed time
    df['ElapDays'] = df.groupby('product')['timestamp'].transform(lambda x: (x.max() - x).dt.days)
    
    return df


# Function for checking whether the review contains images
def image_check(df):
    # Check if the value in the "images" column is an empty list
    df['Image'] = df['images'].apply(lambda x: 0 if x == "[]" else 1)
    return df

# Function for transforming verified purchase column to integer
def verified_purchase(df):
    # Convert boolean values to integers (0 for False, 1 for True)
    df['VerPur'] = df['verified_purchase'].astype(int)
    return df


# Function for updating timestamp information
def extract_timestamp(df):
    # Convert timestamp column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Extract year, month, and day from the timestamp
    df['year'] = df['timestamp'].dt.year
    df['month'] = df['timestamp'].dt.month
    df['hour'] = df['timestamp'].dt.hour

    # Extract the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    
    # Check if the day of the week is Saturday (5) or Sunday (6)
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

    return df


## Applying all functions to the dataframe

def feature_building(df):
    # Apply all individual functions to the DataFrame
    df = calculate_total_helpful_votes(df)
    df = count_pos_tags(df)
    df = word_count(df)
    df = sentence_count(df)
    df = average_words_per_sentence(df)
    df = title_length(df)
    df = calculate_flesch_reading_score(df)
    df = calculate_review_extremity(df)
    df = calculate_elapsed_time(df)
    df = image_check(df)
    df = verified_purchase(df)
    df = extract_timestamp(df)
    return df


