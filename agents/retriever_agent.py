
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

texts = ["Samsung missed earnings", "TSMC beat estimates", "Asia tech stocks rose"]
model = SentenceTransformer('all-MiniLM-L6-v2')
vectors = model.encode(texts)
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(np.array(vectors))

def retrieve(query):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec), 3)
    return [texts[i] for i in I[0]]
