from flask import Flask, request
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec import doc, use_kwargs
from webargs import fields
from repositorio import RepositorioDeArte as repositorio, OK, BAD_REQUEST, NOT_FOUND, CONFLICT, CREATED

app = Flask(__name__)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='API de uma galeria de arte com Python, Flask e Swagger',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    )
})
docs = FlaskApiSpec(app, document_options=False)

@doc(description='Obter lista de todas as obras de arte. Pode ser filtrado por período.', 
     tags=['Obra'],
     params={'anoInicial': {'description': 'Ano inicial do período.', 'in': 'query', 'type': 'int', 'required': False},
            'anoFinal': {'description': 'Ano final do período.', 'in': 'query', 'type': 'int', 'required': False}})
@app.get('/v1/obras')
def get_obras():
    LIMITE = 99999
    ano_inicial = request.args.get('anoInicial', default = -LIMITE, type = int)
    ano_final = request.args.get('anoFinal', default = LIMITE, type = int)
    if ano_inicial != -LIMITE or ano_final != LIMITE:
        return repositorio.listar_obras_por_periodo(ano_inicial, ano_final)
    else:
        return repositorio.listar_todas_obras()

@doc(description='Obter uma obra por ID.', tags=['Obra'])
@app.get('/v1/obra/<int:id>')
def get_obra_id(id):
    encontrado = repositorio.obter_obra_por_id(id)
    return encontrado if encontrado else ({'Erro': 'Não encontrado.'}, NOT_FOUND)

@doc(description='Obter uma obra por Título.', tags=['Obra'])
@app.get('/v1/obras/<string:titulo>')
def get_obras_titulo(titulo):
    return repositorio.obter_obras_por_titulo(titulo)

@doc(description='Obter lista de todos os estilos.', tags=['Estilo'])
@app.get('/v1/estilos')
def get_estilos():
    return repositorio.listar_todos_estilos()

@doc(description='Obter um estilo por ID.', tags=['Estilo'])
@app.get('/v1/estilo/<int:id>')
def get_estilo_id(id):
    encontrado = repositorio.obter_estilo_por_id(id)
    return encontrado if encontrado else ({'Erro': 'Não encontrado.'}, NOT_FOUND)

@doc(description='Obter um estilo por Nome.', tags=['Estilo'])
@app.get('/v1/estilo/<string:nome>')
def get_estilo_nome(nome):
    encontrado = repositorio.obter_estilo_por_nome(nome)
    return encontrado if encontrado else ({'Erro': 'Não encontrado.'}, NOT_FOUND)

@doc(description='Obter obras de um estilo por ID.', tags=['Estilo'])
@app.get('/v1/estilo/<int:id>/obras')
def get_obras_estilo_id(id):
    encontrado = repositorio.obter_estilo_por_id(id)
    return repositorio.listar_obras_por_id_estilo(id) if encontrado else ({'Erro': 'Não encontrado.'}, NOT_FOUND)

@doc(description='Obter obras de um estilo por Nome.', tags=['Estilo'])
@app.get('/v1/estilo/<string:nome>/obras')
def get_obras_estilo_nome(nome):
    encontrado = repositorio.obter_estilo_por_nome(nome)
    return repositorio.listar_obras_por_nome_estilo(nome) if encontrado else ({'Erro': 'Não encontrado.'}, NOT_FOUND)

@doc(description='Inserir um novo estilo.', tags=['Estilo'])
@use_kwargs({'Nome': fields.String()})
@app.post('/v1/estilo')
def post_estilo():
    try:
        nome = request.json['Nome']
        sucesso = repositorio.inserir_estilo(nome)
        return ({'Mensagem': 'Inserido com sucesso.'}, CREATED) if sucesso else ({'Erro': 'Nome do Estilo deve ser único.'}, BAD_REQUEST)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Inserir uma nova obra.', tags=['Obra'])
@use_kwargs({'Titulo': fields.String(), 'Autor': fields.Integer(), 'Ano': fields.Integer(), 'Estilo': fields.Integer(), 'Material': fields.String(), 'UrlImagem': fields.String()})
@app.post('/v1/obra')
def post_obra():
    try:
        titulo = request.json['Titulo']
        autor = request.json['Autor']
        ano = request.json['Ano']
        estilo = request.json['Estilo']
        material = request.json['Material']
        url_imagem = request.json['UrlImagem']
        sucesso = repositorio.inserir_obra(titulo, autor, ano, estilo, material, url_imagem)
        return ({'Mensagem': 'Inserido com sucesso.'}, CREATED) if sucesso else ({'Erro': 'Ids de Autor e Estilo devem existir.'}, BAD_REQUEST)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Editar um estilo por ID.', tags=['Estilo'])
@use_kwargs({'Nome': fields.String()})
@app.put('/v1/estilo/<int:id>')
def put_estilo_id(id):
    if not repositorio.obter_estilo_por_id(id):
        return {'Erro': 'Não encontrado.'}, NOT_FOUND
    try:
        nome = request.json['Nome']
        sucesso = repositorio.editar_estilo_por_id(id, nome)
        return {'Mensagem': 'Editado com sucesso.'} if sucesso else ({'Erro': 'Nome do Estilo deve ser único.'}, BAD_REQUEST)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Editar um estilo por Nome.', tags=['Estilo'])
@use_kwargs({'Nome': fields.String()})
@app.put('/v1/estilo/<string:nome>')
def put_estilo_nome(nome):
    if not repositorio.obter_estilo_por_nome(nome):
        return {'Erro': 'Não encontrado.'}, NOT_FOUND
    try:
        novo_nome = request.json['Nome']
        sucesso = repositorio.editar_estilo_por_nome(nome, novo_nome)
        return {'Mensagem': 'Editado com sucesso.'} if sucesso else ({'Erro': 'Nome deve ser único.'}, BAD_REQUEST)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Editar uma obra por ID.', tags=['Obra'])
@use_kwargs({'Titulo': fields.String(), 'Autor': fields.Integer(), 'Ano': fields.Integer(), 'Estilo': fields.Integer(), 'Material': fields.String(), 'UrlImagem': fields.String()})
@app.put('/v1/obra/<int:id>')
def put_obra_id(id):
    if not repositorio.obter_obra_por_id(id):
        return {'Erro': 'Não encontrado.'}, NOT_FOUND
    try:
        titulo = request.json['Titulo']
        autor = request.json['Autor']
        ano = request.json['Ano']
        estilo = request.json['Estilo']
        material = request.json['Material']
        url_imagem = request.json['UrlImagem']
        sucesso = repositorio.editar_obra_por_id(id, titulo, autor, ano, estilo, material, url_imagem)
        return {'Mensagem': 'Inserido com sucesso.'} if sucesso else ({'Erro': 'Ids de Autor e Estilo devem existir.'}, BAD_REQUEST)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Remover um estilo por id.', tags=['Estilo'])
@app.delete('/v1/estilo/<int:id>')
def delete_estilo_id(id):
    if not repositorio.obter_estilo_por_id(id):
        return {'Erro': 'Não encontrado.'}, NOT_FOUND
    try:
        sucesso = repositorio.remover_estilo_por_id(id)
        return {'Mensagem': 'Removido com sucesso.'} if sucesso else ({'Erro': 'Estilo está sendo usado em obras.'}, CONFLICT)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Remover um estilo por nome.', tags=['Estilo'])
@app.delete('/v1/estilo/<string:nome>')
def delete_estilo_nome(nome):
    if not repositorio.obter_estilo_por_nome(nome):
        return {'Erro': 'Não encontrado.'}, NOT_FOUND
    try:
        sucesso = repositorio.remover_estilo_por_nome(nome)
        return {'Mensagem': 'Removido com sucesso.'} if sucesso else ({'Erro': 'Estilo está sendo usado em obras.'}, CONFLICT)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Remover uma obra por id.', tags=['Obra'])
@app.delete('/v1/obra/<int:id>')
def delete_obra_id(id):
    try:
        sucesso = repositorio.remover_obra_por_id(id)
        return {'Mensagem': 'Removido com sucesso.'} if sucesso else ({'Erro': 'Não Encontrado.'}, NOT_FOUND)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

@doc(description='Alterar URL da Imagem de uma obra por ID.', tags=['Obra'])
@use_kwargs({'UrlImagem': fields.String()})
@app.patch('/v1/obra/<int:id>')
def patch_obra_url_id(id):
    try:
        url_imagem = request.json['UrlImagem']
        sucesso = repositorio.alterar_imagem_obra_por_id(id, url_imagem)
        return {'Mensagem': 'Inserido com sucesso.'} if sucesso else ({'Erro': 'Não Encontrado.'}, NOT_FOUND)
    except (TypeError,KeyError):
        return {'Erro': 'JSON enviado incorreto.'}, BAD_REQUEST

docs.register(get_obras)
docs.register(get_obra_id)
docs.register(get_obras_titulo)
docs.register(get_estilos)
docs.register(get_estilo_id)
docs.register(get_estilo_nome)
docs.register(get_obras_estilo_id)
docs.register(get_obras_estilo_nome)
docs.register(post_estilo)
docs.register(post_obra)
docs.register(put_estilo_id)
docs.register(put_estilo_nome)
docs.register(put_obra_id)
docs.register(delete_estilo_id)
docs.register(delete_estilo_nome)
docs.register(delete_obra_id)
docs.register(patch_obra_url_id)

if __name__ == '__main__':
    app.run(debug=True)