from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from src.config import GOOGLE_API_KEY

def get_embedding_model():
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
    )

    return embedding_model