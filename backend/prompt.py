<<<<<<< HEAD
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful and knowledgeable assistant designed to answer user questions accurately and concisely.\n"
            "Use the provided context and previous conversation to give the most relevant answer. "
            "If the information is not available, respond honestly without making up facts.\n"
            "Answer in simple, clear, and complete sentences.",
        ),
        ("system", "Supporting Document(s): {documents}"),
        ("system", "Chat History: {chat_history}"),
        ("human", "User Question: {question}"),
    ]
)
=======
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful and knowledgeable assistant designed to answer user questions accurately and concisely.\n"
            "Use the provided context and previous conversation to give the most relevant answer. "
            "If the information is not available, respond honestly without making up facts.\n"
            "Answer in simple, clear, and complete sentences.",
        ),
        ("system", "Supporting Document(s): {documents}"),
        ("system", "Chat History: {chat_history}"),
        ("human", "User Question: {question}"),
    ]
)
>>>>>>> old
