<<<<<<< HEAD
from typing_extensions import TypedDict,List,Any
from langchain_core.messages import AnyMessage
from langchain_core.documents import Document

class InputState(TypedDict):
    input:str
    session_id:str


class ProcessState(InputState):
    chat_history: List[AnyMessage]
    documents: List[Document]

class OutputState(TypedDict):
=======
from typing_extensions import TypedDict,List,Any
from langchain_core.messages import AnyMessage
from langchain_core.documents import Document

class InputState(TypedDict):
    input:str
    session_id:str


class ProcessState(InputState):
    chat_history: List[AnyMessage]
    documents: List[Document]

class OutputState(TypedDict):
>>>>>>> old
    result:str