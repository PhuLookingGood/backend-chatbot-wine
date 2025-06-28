from schemas.schemas import MessageRequest
from prompts.rag import question_company


async def findRagCompany(data: MessageRequest):
    result = question_company(data.message)
    return {"received_question": data.message, "answer": result}
