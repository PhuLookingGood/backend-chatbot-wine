from models.langchain_gemini import llm
from api.products import get_products
from api.contacts import get_contacts


def question_product(question: str):
    prompt = f"""ข้อมูลสินค้าจาก API: {get_products()} ข้อมูลผู้ติดต่อจาก API: {get_contacts()} คำถามจากผู้ใช้: {question} กรุณาตอบโดยอิงจากข้อมูลด้านบนเท่านั้น"""
    response = llm.invoke(prompt)
    return response.content
