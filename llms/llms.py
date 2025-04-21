from langchain_groq import ChatGroq
from langchain_google_vertexai import ChatVertexAI
from langchain_mistralai import ChatMistralAI

from settings.settings import  grok_api_key

# Initialize the LLM
model = "llama-3.3-70b-versatile"
model = "llama-3.1-8b-instant"

llm = ChatGroq(model=model, api_key=grok_api_key)

#llm = ChatVertexAI(model="gemini-pro")

#llm = ChatMistralAI(model="mistral-large-latest")
