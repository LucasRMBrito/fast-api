def produtoEntidade(item) -> dict:
    return {
        '_id': str(item['_id']),
        'item': item['item'],
        'preco_unitario': item['preco_unitario'],
        'quantidade': item['quantidade']
    }

def produtosEntidade(itens) -> list:
    return [produtoEntidade(item) for item in itens]