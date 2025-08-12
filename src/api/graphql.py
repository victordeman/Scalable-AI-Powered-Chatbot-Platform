import strawberry
from src.llm.chatbot import Chatbot

@strawberry.type
class ChatResponse:
    response: str

@strawberry.type
class Query:
    @strawberry.field
    async def chat(self, message: str) -> ChatResponse:
        chatbot = Chatbot()
        response = chatbot.process_message(message)
        return ChatResponse(response=response)

schema = strawberry.Schema(query=Query)
