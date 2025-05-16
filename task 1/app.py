# Streamlit app entry point
import streamlit as st
from analytics.topic_analysis import get_common_topics
from analytics.sentiment_analysis import average_rating

st.title("Chatbot Analytics Dashboard")
log_path = "data/user_logs.json"

st.metric("Total Queries", sum(1 for line in open(log_path)))
st.write("**Most Common Topics:**", get_common_topics(log_path))
st.metric("Avg. Satisfaction Rating", round(average_rating(log_path), 2))
