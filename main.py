from src.ingestion.pipeline import ingest_document
from src.rag.chain import create_rag_pipeline
from src.ingestion.embeddings import get_embedding_model
from src.ingestion.vector_store import load_vector_store

import streamlit as st

from langchain_chroma import Chroma

from time import sleep
from pathlib import Path

embeddings= get_embedding_model()

st.set_page_config(
    page_title="DocAnalyzer",
    page_icon="📃"
)

st.title("📄 DocAnalyzer")
st.caption("Upload a PDF and ask questions about your document.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

# Before Document Uploaded UI

MAX_FILE_SIZE_MB = 10

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

if not st.session_state.document_uploaded:
    file = st.file_uploader(
        label="Select your PDF doc",
        type="pdf"
    )

    if file is not None:
        file_size_mb = file.size / (1024 * 1024)

        if file_size_mb > MAX_FILE_SIZE_MB:
            st.error(f"❌ File size must be less than {MAX_FILE_SIZE_MB} MB")
            st.stop()

    if file:
        file_path = UPLOAD_DIR / file.name
        with open(file_path, "wb") as f:
            f.write(file.getvalue())

        with st.spinner('Processing...'):
            ingest_document(str(file_path))
        
        st.markdown("Document Processed Successfully!")

        st.session_state.document_uploaded = True

        sleep(2)
        st.rerun()

# After Document Uploaded UI
if st.session_state.document_uploaded:

    for msg in st.session_state.messages:
        role = msg['role']
        content = msg['content']

        st.chat_message(role).markdown(content)

    query = st.chat_input("Ask Anything on PDF!")

    if query:
        st.session_state.messages.append({
            'role': 'user',
            'content': query
        })

        st.chat_message("user").markdown(query)
        vector_store = load_vector_store()

        rag = create_rag_pipeline(vector_store=vector_store)

        with st.spinner("Thinking⚡..."):
            response = rag(query)

        st.session_state.messages.append({
            'role': 'ai',
            'content': response['answer']
        })
        st.chat_message("ai").markdown(response['answer'])