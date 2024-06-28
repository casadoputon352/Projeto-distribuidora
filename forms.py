from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Email


class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    submit = SubmitField('Salvar')


class ProdutoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    preco = FloatField('Preço', validators=[DataRequired()])
    estoque = IntegerField('Estoque', validators=[DataRequired()])
    submit = SubmitField('Salvar')


class PedidoForm(FlaskForm):
    data = DateTimeField('Data do Pedido', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    cliente_id = IntegerField('ID do Cliente', validators=[DataRequired()])
    submit = SubmitField('Salvar')
