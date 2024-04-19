import spacy
import pandas as pd
from readability import Readability

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



# Function for Number of sentences in a review (Nsents) 
def sentence_count(df):
    # Define a function to count the number of sentences in a review
    def word_count(text):
        # Split the text into sentences
        sentences = text.split(".")
        
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence]
        
        return len(sentences)

    # Apply the function to the 'text' column to calculate sentence counts
    df['sentence_count'] = df['text'].apply(word_count)
    return df



def add_average_sentence_length(df):
    # Define a function to calculate the average length of sentences in terms of words
    def calculate_average_length_of_sentences(text):
        # Call the existing function to count sentences
        num_sentences = sentence_count(text)

        # Avoid division by zero
        if num_sentences == 0:
            return 0

        # Split the text into words
        words = text.split()

        # Calculate the average length of sentences in terms of words
        average_length_of_sentences = len(words) / max(1, num_sentences)

        return average_length_of_sentences

    # Apply the function to the 'text' column to calculate average sentence length
    df['avg_sentence_length'] = df['text'].apply(calculate_average_length_of_sentences)
    return df



# Function for Title Length (TL)
def title_length(df):
    # Count the number of titles
    df['title_length'] = df['title_x'].apply(lambda x: len(x))
    return df



# Function for calculating the Flesch-Kincaid score
def calculate_flesch_kincaid(df):
    # Initialize Readability object with the text
    readability_scores = []

    for text in df['text']:
        r = Readability(text)
        # Calculate the Flesch-Kincaid score
        score = r.flesch_kincaid().score
        readability_scores.append(score)

    # Add the Flesch-Kincaid score as a new column to the DataFrame
    df['F–K_score'] = readability_scores
    return df



# Function for calculating the review extremity score (Difference between avg Rating and Rating)
def calculate_review_extremity(df):
    # Calculate the review extremity as the difference between review rating and average product rating
    df['review_extremity'] = df['rating'] - df['average_rating']
    return df


# Function for calculating the Elapsed Time (ET) between the review and the product release
def calculate_elapsed_time(df):
    # Convert timestamp column to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Find the most recent date in the 'timestamp' column
    recent_date = df['timestamp'].max()
    
    # Convert the recent date to Unix time format
    recent_unix_time = recent_date.timestamp()
    
    # Calculate elapsed time for each review
    df['elapsed_time'] = (recent_unix_time - df['timestamp']).dt.total_seconds()
    
    return df



## Applying all functions to the dataframe

def feature_building(df):
    # Apply all individual functions to the DataFrame
    df = calculate_helpful_ratio(df)
    df = count_pos_tags(df)
    df = word_count(df)
    df = sentence_count(df)
    df = add_average_sentence_length(df)
    df = title_length(df)
    df = calculate_flesch_kincaid(df)
    df = calculate_review_extremity(df)
    df = calculate_elapsed_time(df)

    return df
