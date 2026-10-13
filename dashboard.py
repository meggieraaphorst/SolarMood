import streamlit as st
import pandas as pd

# Page title
st.title("☀️ SolarMood")
st.write("Solar Energy News Sentiment Dashboard")

# Load collected news data
df = pd.read_csv("solarmood.csv")

# Show total number of articles
st.metric("Total articles", len(df))

# Show sentiment distribution
st.subheader("News Sentiment")

sentiment_counts = df["sentiment"].value_counts()
st.bar_chart(sentiment_counts)

# Show collected articles
st.subheader("Collected News Articles")
st.dataframe(df)
