import streamlit as st
import pandas as pd
import numpy as np
import pickle
from utils import embed_texts, build_faiss_index, search_index

# Load or preprocess dataset (example: CSV with columns: 'title', 'abstract')
@st.cache_data
def load_data():
    df = pd.read_csv('data/arxiv_subset.csv')  # Use a small subset for testing
    return df

@st.cache_resource
def prepare_index(df):
    texts = df['abstract'].tolist()
    embeddings = embed_texts(texts)
    index = build_faiss_index(embeddings)
    return index, embeddings

def main():
    st.title("Arxiv Papers Chatbot")
    df = load_data()
    index, embeddings = prepare_index(df)

    user_query = st.text_input("Ask me about scientific papers:")
    if user_query:
        query_embedding = embed_texts([user_query])[0]
        results_idx = search_index(index, query_embedding, top_k=3)
        
        st.write("Top related papers:")
        for idx in results_idx:
            st.markdown(f"**{df.iloc[idx]['title']}**")
            st.write(df.iloc[idx]['abstract'][:300] + '...')

if __name__ == "__main__":
    main()
