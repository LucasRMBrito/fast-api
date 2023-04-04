from fastapi import APIRouter, HTTPException
from models.produto import Produto
from config.db import colecao
from schemas.produto import produtoEntidade, produtosEntidade
from bson import ObjectId

produto = APIRouter()


@produto.get('/')
async def home():
    return "/produtos"


@produto.get('/produtos')
async def mostrar_produtos():
    itens = produtosEntidade(colecao.find())
    return {"status": "ok" , "data": itens}


@produto.get('/produtos/{id_produto}')
async def pegar_produto(id_produto: str):
    produto = produtosEntidade(colecao.find({"_id": ObjectId(id_produto)}))
    return {"status": "ok", "data": produto}


@produto.post('/produtos')
async def adicionar_produto(produto: Produto):
    _id = colecao.insert_one(dict(produto))
    produto = produtosEntidade(colecao.find({"_id": _id.inserted_id}))
    return {"status": "ok", "data": produto}


@produto.put('/produtos/{id_produto}')
async def atualizar_produto(id_produto: str, produto: Produto):
    colecao.find_one_and_update({"_id": ObjectId(id_produto)}, {
        "$set": dict(produto)
    })
    produto = produtosEntidade(colecao.find({"_id": ObjectId(id_produto)}))
    return {"status": "ok", "data": produto}


@produto.delete('/produtos/{id_produto}')
async def deletar_produto(id_produto: str):
    colecao.find_one_and_delete({"_id": ObjectId(id_produto)})
    return {"status": "ok", "data": []}
