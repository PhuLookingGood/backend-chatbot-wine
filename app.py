from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models.langchain_gemini import generate_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageRequest(BaseModel):
    message: str


@app.post("/answer")
async def receive_answer(data: MessageRequest):
    result = generate_answer(data.message)
    print(result)
    return {"received_question": data.message, "answer": result}
