# 1MLET_FASE1_TECH_CHALLANGE

Grupo 43:
Bruno
Pedro
Rodrigo
Alberto
Daniela

<hr>
Portugues

## Requisitos:

### Seus objetivos incluem:
* #### Criar uma Rest API em Python que faça a consulta no site da Embrapa.
* #### Sua API deve estar documentada.
* #### É recomendável (não obrigatório) a escolha de um método de autenticação (JWT, por exemplo).
* #### Criar um plano para fazer o deploy da API, desenhando a arquitetura do projeto desde a ingestão até a alimentação do modelo (aqui não é necessário elaborar um modelo de ML, mas é preciso que vocês escolham um cenário interessante em que a API possa ser utilizada).
* #### Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github.

<hr>

Ingles:

## Requirements

### Your goals include:
* #### Creating a REST API in Python that queries the Embrapa website.
* #### Your API must be documented.
* #### It is recommended (but not mandatory) to choose an authentication method (JWT, for example).
* #### Create a plan for deploying the API, designing the project architecture from ingestion to feeding the model (it is not necessary to develop an ML model here, but you need to choose an interesting scenario in which the API can be used).
* #### Make an MVP by deploying it with a shareable link and a GitHub repository.


<hr>

# Docker

Comando para criar imagem: 
- Exemplo: `docker build -t <image_name> .`


- Prod: `docker build -t 1mlet .`


Comando para rodar o conteiner (Exposed)
- Exemplo: ` docker run -d -p <n_port>:<n_port> --name <container_name> <image_name>`


- Prod (Exposto): ` docker run -d -p 8000:8000 --name c_1mlet 1mlet`
- Prod: ` docker run -d --name c_1mlet 1mlet`