from scrape import get_india_headlines
from analyze import analyze_headlines
import pandas as pd

def run():
    headlines = get_india_headlines()
    sentiments, keywords = analyze_headlines(headlines)

    df = pd.DataFrame({
        "Headline": headlines,
        "Sentiment": sentiments
    })
    df.to_csv("today_trends_india.csv", index=False)

    print("Top 5 Keywords:")
    for word, count in keywords[:5]:
        print(f"{word}: {count} times")

    print("\nSentiment Summary:")
    print(df["Sentiment"].value_counts())

if __name__ == "__main__":
    run()
