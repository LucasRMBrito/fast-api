from fastapi import FastAPI, HTTPException
from routes.produto import produto

app = FastAPI()
app.include_router(produto)