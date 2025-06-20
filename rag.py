from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# โหลดเอกสาร
loader = TextLoader(
    "/home/phuthanet/chatbot/chatbot_wine/backend/data.txt", encoding="utf-8"
)

# เอาเอกสารมาใช้งาน
documents = loader.load()
# print(documents)

# แบ่งเอกสารเป็นส่วนย่อย (Chunk)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)

# จำนวนเอกสารที่แบ่งย่อยแล้ว
chunks = text_splitter.split_documents(documents)
# for i, chunk in enumerate(chunks):
#     print(f"chunk: {i + 1}, {chunk.page_content}")

# ตัวแปลงข้อมูลเป็นเวกเตอร์
embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", api_key=os.getenv("GOOGLE_API_KEY")
)

# เก็บข้อมูลงใน Vector store
vector_store = FAISS.from_documents(chunks, embedding)

# ตัวดึงข้อมูลจาก Store ไปใช้งาน (Retrievers)
retrievers = vector_store.as_retriever()

# Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "ใช้ข้อมูลจากเอกสารในการตอบคำถามให้สั้นกระชับด้วยความสุภาพเป็นกันเอง"),
        ("human", "คำถาม : {question} , ข้อมูลที่เกี่ยวข้อง : {context}"),
    ]
)

# สร้าง Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,  # ระดับความคิดสร้างสรรค์ 0 - 2
    api_key=os.getenv("GOOGLE_API_KEY"),
)

# Chain
# ใช้ RunnablePassthrough เพื่อให้คำถามมาจากผู้ใช้โดยไม่กำหนดเอง
rag_chain = (
    {"context": retrievers, "question": RunnablePassthrough()}
    # เรียกใช้ prompt => llm => ตอบกลับมาเป็น (StrOutputParser)
    | prompt
    | llm
    | StrOutputParser()
)

result = rag_chain.invoke("ขอข้อมูลที่สำคัญของบริษัท")
print(result)
