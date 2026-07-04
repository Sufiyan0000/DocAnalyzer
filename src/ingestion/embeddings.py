from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import GOOGLE_API_KEY

def get_embedding_model():
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        api_key= GOOGLE_API_KEY,
    )

    return embedding_model