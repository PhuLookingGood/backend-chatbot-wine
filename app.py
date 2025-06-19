from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.products import router as product

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product)
