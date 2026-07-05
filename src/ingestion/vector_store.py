from .embeddings import get_embedding_model

from langchain_chroma import Chroma

CHROMA_PATH =  "./data/chroma"
COLLECTION_NAME = "documents"

def create_vector_store(documents):
    embeddings = get_embedding_model()

    # Connect to Chroma
    vector_store = Chroma(
        collection_name= COLLECTION_NAME,
        embedding_function= embeddings,
        persist_directory= CHROMA_PATH
    )

    # Delete Old collection
    try:
        vector_store.delete_collection()
    except ValueError:
        pass

    # Create fresh collection with new PDF
    vector_store = Chroma.from_documents(
        documents= documents,
        embedding= embeddings,
        collection_name= COLLECTION_NAME,
        persist_directory= CHROMA_PATH
    )


    return vector_store

def load_vector_store():
    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name= COLLECTION_NAME,
        embedding_function= embeddings,
        persist_directory= CHROMA_PATH
    )

    return vector_store