from flask import current_app as app, render_template
from .controllers import (listar_clientes, adicionar_cliente, excluir_cliente_view, listar_pedidos, adicionar_pedido,
                          excluir_pedido_view)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clientes')
def clientes():
    return listar_clientes()


@app.route('/clientes/novo', methods=['GET', 'POST'])
def novo_cliente():
    return adicionar_cliente()


@app.route('/clientes/excluir/<int:cliente_id>', methods=['POST'])
def excluir_cliente(cliente_id):
    return excluir_cliente_view(cliente_id)


@app.route('/pedidos')
def pedidos():
    return listar_pedidos()


@app.route('/pedidos/novo', methods=['GET', 'POST'])
def novo_pedido():
    return adicionar_pedido()


@app.route('/pedidos/excluir/<int:pedido_id>', methods=['POST'])
def excluir_pedido(pedido_id):
    return excluir_pedido_view(pedido_id)
