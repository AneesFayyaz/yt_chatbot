import os
import faiss
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, path, embedding_model):
    embeddings = OpenAIEmbeddings(model=embedding_model)
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(path)
    return vector_store

def load_vector_store(path, embedding_model):
    if not os.path.exists(path):
        raise FileNotFoundError("Vector store not found. Please build it first.")
    embeddings = OpenAIEmbeddings(model=embedding_model)
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
