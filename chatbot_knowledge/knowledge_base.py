import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load a pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 768  # Dimension of sentence embeddings
index = faiss.IndexFlatL2(dimension)

knowledge_base = []  # List to store texts and their embeddings

# Convert text to embedding
def text_to_embedding(text):
    return model.encode([text])

# Add new information to the knowledge base
def add_to_knowledge_base(texts, embeddings):
    global knowledge_base
    knowledge_base.extend(zip(texts, embeddings))
    faiss.normalize_L2(embeddings)
    index.add(embeddings)

# Function to update the knowledge base with new data
def update_knowledge_base(new_texts):
    embeddings = np.array([text_to_embedding(text) for text in new_texts])
    add_to_knowledge_base(new_texts, embeddings)

# Function to search the knowledge base
def search_knowledge_base(query):
    query_embedding = text_to_embedding(query)
    D, I = index.search(query_embedding, k=5)  # Top 5 results
    results = [knowledge_base[i] for i in I[0]]
    return results
