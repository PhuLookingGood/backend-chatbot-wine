from schemas.schemas import MessageRequest
from models.langchain_gemini import question_product


async def findAll(data: MessageRequest):
    result = question_product(data.message)
    return {"received_question": data.message, "answer": result}
