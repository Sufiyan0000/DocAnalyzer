from .embeddings import get_embedding_model

from langchain_chroma import Chroma

def create_vector_store(documents):
    embeddings = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents= documents,
        embedding= embeddings,
        collection_name= "documents",
        persist_directory= "./data/chroma"
    )


    return vector_store
