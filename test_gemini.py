import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env
load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
   
    temperature=0
)

# Ask a question
response = llm.invoke("Introduce yourself in 3 lines.")

print(response.content)
