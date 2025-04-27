from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

gemini = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
