from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from src.llm.chatbot import Chatbot

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

async def get_chatbot():
    return Chatbot()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, chatbot: Chatbot = Depends(get_chatbot)):
    try:
        response = chatbot.process_message(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
