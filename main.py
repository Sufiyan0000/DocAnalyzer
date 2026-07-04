from src.ingestion.pipeline import ingest_document
from src.rag.chain import create_rag_pipeline

vector_store = ingest_document('./my_resume.pdf')
rag_pipeline = create_rag_pipeline(vector_store)

question = input("Ask a question: ")

response= rag_pipeline(question)

print("\n Answer: ")
print(response['answer'])

print("\n Sources: ")

for document in response['documents']:
    print(document.metadata)