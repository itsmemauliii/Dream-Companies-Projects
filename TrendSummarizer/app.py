import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scrape import get_india_headlines
from analyze import analyze_headlines

st.set_page_config(page_title="India TrendSummarizer", layout="wide")
st.title("📰 India's Trending News Summary")

headlines = get_india_headlines()
sentiments, keywords = analyze_headlines(headlines)

df = pd.DataFrame({
    "Headline": headlines,
    "Sentiment": sentiments
})
sentiment_counts = df["Sentiment"].value_counts()

# Top keywords
st.subheader("🔑 Top 5 Trending Keywords")
for word, count in keywords[:5]:
    st.write(f"• **{word}** – {count} times")

# Sentiment Pie Chart
st.subheader("📊 Sentiment Distribution")
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Sample Headlines
st.subheader("📰 Sample Headlines Analyzed")
st.dataframe(df.head(10))
