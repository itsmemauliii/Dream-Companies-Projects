from textblob import TextBlob
from collections import Counter

def analyze_headlines(headlines):
    sentiments = []
    all_words = []

    for line in headlines:
        blob = TextBlob(line)
        polarity = blob.sentiment.polarity

        # Classify tone
        if polarity > 0.1:
            sentiments.append("Positive")
        elif polarity < -0.1:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")

        # Collect clean words
        all_words += [word.lower() for word in blob.words if word.isalpha() and len(word) > 3]

    # Top 10 keywords
    keyword_counts = Counter(all_words).most_common(10)
    return sentiments, keyword_counts
