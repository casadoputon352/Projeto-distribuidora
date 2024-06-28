from flask import render_template, redirect, url_for, flash
from . import db
from .models import Cliente, Pedido, ItemPedido
from .forms import ClienteForm, PedidoForm


def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('listar_clientes.html', clientes=clientes)


def adicionar_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(nome=form.nome.data, email=form.email.data, telefone=form.telefone.data)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente adicionado com sucesso!')
        return redirect(url_for('clientes'))
    return render_template('adicionar_cliente.html', form=form)


def excluir_cliente_view(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    flash('Cliente excluído com sucesso!', 'success')
    return redirect(url_for('clientes'))


def listar_pedidos():
    pedidos = Pedido.query.all()
    return render_template('listar_pedidos.html', pedidos=pedidos)


def adicionar_pedido():
    form = PedidoForm()
    if form.validate_on_submit():
        pedido = Pedido(data=form.data.data, cliente_id=form.cliente_id.data)
        db.session.add(pedido)
        db.session.commit()
        flash('Pedido adicionado com sucesso!', 'success')
        return redirect(url_for('pedidos'))
    return render_template('adicionar_pedido.html', form=form)


def excluir_pedido_view(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    db.session.delete(pedido)
    db.session.commit()
    flash('Pedido excluído com sucesso!', 'success')
    return redirect(url_for('pedidos'))
