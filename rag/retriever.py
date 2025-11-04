from utils.vector_store import load_vector_store
from config.settings import VECTOR_STORE_PATH, EMBEDDING_MODEL

def get_retriever():
    vector_store = load_vector_store(VECTOR_STORE_PATH, EMBEDDING_MODEL)
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})
    return retriever
