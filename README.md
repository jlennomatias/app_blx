App BLX

app para anuncio de vendas de produtos na vizinhança

Functionalidades:
    .Qualquer pessoa poderá anunciar produtos
    . Qualquer pessoa poderá fazer pedidos dos produtos anunciados
    . Uma pessoa tem:
        . nome
        . telefone
        . senha
    . Um produto tem:
        . nome
        . detalhamento
        . preço
        . disponibilidade (sim/não)
        . fotos
    . Um pedido tem:
        . produto
        . pessoa que está pedindo
        . quantidade
        . local de entrega
        . observações (sabor, horario de entrega, troco, etc)
    . Cada usuario terpa uma lista de pedidos recebidos e pedidos feitos.
    . O pedido deverá ser aceito pelo vendedor
    . O comprador poderá acompanhar seus pedidos:
        . status(feito, aceito)

Arquitetura e ferramentas
    . Python + FastAPI
    . Será uma API REST
    . Banco de dados: Postgresql e/ou Mongodb
    Docker para o banco de dados
    MVC
    DDD e Arquitetura Limpa