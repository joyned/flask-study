# Projeto API Flask

Esse é um projeto para estudo.

## Instalação

Abra o terminal/cmd e vá na pasta do projeto.

Execute o seguinte comando:

```bash
pip install requirements.txt
```

## Como funciona?
A biblioteca Flask é usada para criar uma API em Python.

O arquivo ``rest.py`` irá conter todos seus endpoints.

Abaixo, estarei dando alguns exemplos de endpoints.

```python

@rest.route('/endpoint/get', methods=['GET'])
def your_get_method():
    # Do something...
    return jsonify("YOUR_RETURN")


# With body content
@rest.route('/endpoint/post/body', methods=['POST'])
def your_post_method_with_body():
    data = request.get_json()
    # Do something...
    return jsonify("YOUR_RETURN")

# With query param
@rest.route('/endpoint/post/query/<param>', methods=['POST'])
def your_post_method_with_query_param(param):
    # Do something...
    return jsonify("YOUR_RETURN")

```
É sempre necessário e retornar algo, caso não retorne, irá ocorrer um erro.

Dica: Não precisa subir a API a cada modificação, o próprio Flask já entende as modificações e faz o reload da aplicação.

## Como testar?

Usar o Postman para fazer as chamadas. Lembre-se que precisa estar atento ao verbo HTTP que se está usando naquele endpoint.

Por exemplo: Um endpoint que está definido como '/endpoint/get' e o método dele é GET, não pode receber chamadas usando o metodo POST.

A URL que você ira usar, por padrão, é a ``http://127.0.0.1:5000/SEU-ENDPOINT``.

Usando o exemplo acima, sua URL de chamada seria ``http://127.0.0.1:5000/endpoint/get``.

## Desafio

Nesse desafio não iremos usar banco de dados, vamos fazer tudo em memória.

##### 1) Crie uma lista global que ira armazenar nomes de heróis.
- Criar um endpoint que ira retornar o nome de todos os heróis que estão nessa lista.
- Criar um endpoint para adicionar um herói nessa lista, utilizando o método POST que ira receber o nome do herói no body.
- Criar um endpoint que ira buscar um herói nessa lista, o nome do herói deve ser passado na URL. Retornar uma mensagem amigável explicando se achou ou não esse herói.
- Criar um endpoint para remover o herói dessa lista. Caso o herói que o usuário deseja remover não exista, retornar uma mensagem explicando. Caso o herói exista na lista e a remoção tenha sido feita com sucesso, retornar a lista de heróis atualizada.
