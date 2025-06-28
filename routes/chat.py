from fastapi import APIRouter
from schemas.schemas import MessageRequest
from controllers.products import findAll
from controllers.rag import findRagCompany
from controllers.chat import detect_intent

router = APIRouter()


@router.post("/chat")
async def chat_router(data: MessageRequest):
    intent = await detect_intent(data.message)

    if intent == "product":
        return await findAll(data)
    elif intent == "company":
        return await findRagCompany(data)
    else:
        return {"answer": "ขออภัย ไม่สามารถระบุความต้องการของคุณได้"}
