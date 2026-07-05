from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

def create_llm():
    return ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)