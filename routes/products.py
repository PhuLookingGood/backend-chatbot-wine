from fastapi import APIRouter
from schemas.schemas import MessageRequest
from controllers.products import findAll

router = APIRouter()


@router.post("/answer")
async def product(data: MessageRequest):
    return await findAll(data)
