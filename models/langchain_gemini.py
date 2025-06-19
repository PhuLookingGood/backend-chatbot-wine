import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from api.products import get_products
from api.contacts import get_contacts

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=1,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


def generate_answer(question: str):
    prompt = f"""ข้อมูลสินค้าจาก API: {get_products()} ข้อมูลผู้ติดต่อจาก API: {get_contacts()} คำถามจากผู้ใช้: {question} กรุณาตอบโดยอิงจากข้อมูลด้านบนเท่านั้น"""
    response = llm.invoke(prompt)
    print(response.content)
    return response.content
