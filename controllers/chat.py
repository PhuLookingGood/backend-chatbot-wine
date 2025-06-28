from models.langchain_gemini import llm


async def detect_intent(question: str):
    prompt = f"""
    จงตอบว่า "product" หรือ "company" เท่านั้น โดยวิเคราะห์จากคำถามนี้: "{question}"
    - ถ้าเป็นคำถามเกี่ยวกับสินค้า ตอบว่า "product" หรือข้อมูลเกี่ยวกับสินค้า
    - ถ้าเป็นคำถามเกี่ยวกับข้อมูลบริษัท ตอบว่า "company" หรือข้อมูลที่เกียวกับร้าน 
    """
    result = llm.invoke(prompt)
    return result.content
