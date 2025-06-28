from fastapi import APIRouter
from schemas.schemas import MessageRequest
from controllers.rag import findRagCompany

router = APIRouter()


@router.post("/send-rag")
async def rag_company(data: MessageRequest):
    return await findRagCompany(data)
