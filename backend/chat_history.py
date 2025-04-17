from langchain_mongodb.chat_message_histories import MongoDBChatMessageHistory
import logging
from pymongo import errors
import json
logger = logging.getLogger(__name__)


class ChatHistoryManager(MongoDBChatMessageHistory):

    def update_session_id(self, session_id):
        self.session_id = session_id

    @property
    def current_chat_history(self):
        chat_history = self.messages[::-1][:8]
        return chat_history

    def find_chat_history(self, session_id):
        cursor = self.collection.find({self.session_id_key: session_id})
        chat_history = []
        if cursor:
            for document in cursor:
                history = json.loads(document["History"])
                chat_history.append(
                    {
                        "type": history["type"],
                        "content": history["data"]["content"],
                    }
                )
        return chat_history
    
    
    @property
    def all_chat_history(self):
        cursor = self.collection.aggregate(
            [{"$group": {"_id": "$SessionId", "entries": {"$push": "$$ROOT"}}}]
        )

        full_history = {}
        if cursor:
            for document in cursor:
                full_history[document["_id"]] = []
                for entry in document["entries"]:
                    history = json.loads(entry["History"])
                    full_history[document["_id"]].append(
                        {
                            "type": history["type"],
                            "content": history["data"]["content"],
                        }
                    )

        return full_history

    def clear(self, session_id) -> None:
        """Clear session memory from MongoDB"""
        try:
            self.collection.delete_many({self.session_id_key: session_id})
        except errors.WriteError as err:
            logger.error(err)
