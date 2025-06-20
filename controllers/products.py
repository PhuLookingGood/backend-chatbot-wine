from schemas.schemas import MessageRequest
from prompts.products import question_product


async def findAll(data: MessageRequest):
    result = question_product(data.message)
    return {"received_question": data.message, "answer": result}
