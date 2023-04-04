from pydantic import BaseModel

class Produto(BaseModel):
    item: str
    preco_unitario: float
    quantidade: int
