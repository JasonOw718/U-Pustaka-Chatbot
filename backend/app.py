from fastapi import FastAPI, WebSocket
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from langgraph.graph import START, StateGraph, END
from state import InputState, ProcessState, OutputState
from node import (
    update_chat_history,
    generate_response,
    retrieve_document,
    chat_history_manager,
)
from starlette.websockets import WebSocketDisconnect

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


def initialize_route():

    builder = StateGraph(ProcessState, input=InputState, output=OutputState)
    builder.add_node("update_chat_history", update_chat_history)
    builder.add_node("generate_response", generate_response)
    builder.add_node("retrieve_document", retrieve_document)
    builder.add_edge(START, "update_chat_history")
    builder.add_edge("update_chat_history", "retrieve_document")
    builder.add_edge("retrieve_document", "generate_response")
    builder.add_edge("generate_response", END)
    graph = builder.compile()

    @app.websocket("/stream")
    async def stream_response(websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                request = await websocket.receive_json()
                question = request.get("question")
                session_id = request.get("sessionId")
                for message, metadata in graph.stream(
                    {"input": question, "session_id": session_id},
                    stream_mode="messages",
                ):
                    if metadata["langgraph_node"] == "generate_response":
                        await websocket.send_text(message.content)

        except WebSocketDisconnect:
            print("Client disconnected")

    @app.get("/chat-history/{session_id}")
    async def get_chat_history_by_session(session_id: str):
        chat_history_manager.update_session_id(session_id)
        return {"chat_history": chat_history_manager.find_chat_history(session_id)}

    @app.get("/chat-history")
    async def get_all_chat_history():
        return {"all_chat_history": chat_history_manager.all_chat_history}
    
    @app.delete("/chat-history/{session_id}")
    async def delete_chat_history_by_session(session_id: str):
        chat_history_manager.clear(session_id)
        return {"message": f"Chat history for session {session_id} has been deleted"}


if __name__ == "__main__":
    initialize_route()
    uvicorn.run(app, host="localhost", port=8000)
