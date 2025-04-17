from state import InputState, ProcessState, OutputState
from chat_history import ChatHistoryManager
from prepare_retriever import prepare_retriever
from prompt import prompt
from models import gemini
import os

DATABASE_URL = os.getenv("DATABASE_URL")
chat_history_manager = manager = ChatHistoryManager(
    DATABASE_URL, "", "practice", "chat_history"
)


def update_chat_history(state: InputState) -> ProcessState:
    chat_history_manager.update_session_id(state["session_id"])
    chat_history_manager.add_user_message(state["input"])
    return {"chat_history": chat_history_manager.current_chat_history}


def retrieve_document(state: ProcessState) -> ProcessState:
    retriever = prepare_retriever()
    result = retriever.invoke(state["input"])
    return {"documents": result}


def generate_response(state: ProcessState) -> OutputState:
    chain = prompt | gemini
    response = chain.invoke(
        {
            "question": state["input"],
            "documents": state["documents"],
            "chat_history": state["chat_history"],
        }
    )
    chat_history_manager.add_ai_message(response.content)
    return {"result": response.content}
