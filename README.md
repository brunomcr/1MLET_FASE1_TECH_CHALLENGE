# 1MLET_FASE1_TECH_CHALLENGE

Group 43:
Bruno
Pedro
Rodrigo
Alberto
Daniela

<br>

## Requirements

### Your goals include:
* #### Creating a REST API in Python that queries the Embrapa website.
* #### Your API must be documented.
* #### It is recommended (but not mandatory) to choose an authentication method (JWT, for example).
* #### Create a plan for deploying the API, designing the project architecture from ingestion to feeding the model (it is not necessary to develop an ML model here, but you need to choose an interesting scenario in which the API can be used).
* #### Make an MVP by deploying it with a shareable link and a GitHub repository.

<br>

## Solution Architecture Diagram

![1MLET_FASE1_TECH_CHALLENGE.drawio.png](assets%2Fimages%2F1MLET_FASE1_TECH_CHALLENGE.drawio.png)


## Subsystem Sequence Diagram 

![uml.drawio.png](assets%2Fimages%2Fuml.drawio.png)

<br>

## Docker

Build:
`$ docker build -t 1mlet .`

Run:
- With port exposed
`$docker run -d -p 8000:8000 --name c_1mlet 1mlet`
- Without port exposed
`$docker run -d --name c_1mlet 1mlet`

Compose (includes database integration):
`$ docker-compose up -d`
