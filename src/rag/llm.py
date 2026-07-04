from langchain_google_genai import ChatGoogleGenerativeAI

def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature= 0.3
    )