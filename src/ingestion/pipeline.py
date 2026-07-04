from .loader import load_pdf
from .splitter import split_documents
from .vector_store import create_vector_store

def ingest_document(documents):

    documents = load_pdf(documents)

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    return vector_store
