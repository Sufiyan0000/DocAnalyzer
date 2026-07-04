from langchain_google_genai import ChatGoogleGenerativeAI

from .prompts import RAG_PROMPT
from .retriever import create_retriever
from .llm import create_llm

def format_documents(documents):
    return "\n\n".join(
        document.page_content
        for document in documents
    )


def create_rag_pipeline(vector_store):
    llm = create_llm()

    retriever = create_retriever(vector_store)

    def answer_question(question):
        documents = retriever.invoke(question)

        context = format_documents(documents)

        prompt = RAG_PROMPT.invoke(
            {
                "context": context,
                "question": question
            }
        )

        response = llm.invoke(prompt)

        return {
            "answer": response.content,
            "documents": documents
        }

    return answer_question