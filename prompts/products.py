from models.langchain_gemini import llm
from api.products import get_products
from api.contacts import get_contacts


def question_product(question: str):
    products = get_products()
    contacts = get_contacts()

    prompt = f""" คุณคือตัวช่วยแนะนำสินค้าจากร้านไวน์ โปรดตอบด้วยน้ำเสียงสุภาพ กระชับ เป็นกันเอง โดยอ้างอิงจากข้อมูลที่ให้ไปเท่านั้น
            คำถาม:{question} ข้อมูลสินค้า:{products} ข้อมูลผู้ติดต่อ:{contacts} """

    response = llm.invoke(prompt)
    return response.content
