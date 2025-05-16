import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Initialize model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def embed_texts(texts):
    return model.encode(texts, convert_to_numpy=True)

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def search_index(index, query_embedding, top_k=5):
    D, I = index.search(np.array([query_embedding]), top_k)
    return I[0]
