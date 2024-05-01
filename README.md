# 1MLET_FASE1_TECH_CHALLENGE

## Overview

This API is part of the Machine Learning Engineering FIAP Pos-Tech program. 
It provides a programmatic way to access data from the Embrapa website amd allows users to retrieve relevant information through well-defined endpoints.

## Project Requirements

* #### Creating a REST API in Python that queries the Embrapa website.
* #### Your API must be documented.
* #### It is recommended (but not mandatory) to choose an authentication method (JWT, for example).
* #### Create a plan for deploying the API, designing the project architecture from ingestion to feeding the model (it is not necessary to develop an ML model here, but you need to choose an interesting scenario in which the API can be used).
* #### Make an MVP by deploying it with a shareable link and a GitHub repository.

## Solution Architecture Diagram

![1MLET_FASE1_TECH_CHALLENGE.drawio.png](assets%2Fimages%2F1MLET_FASE1_TECH_CHALLENGE.drawio.png)

## Subsystem Sequence Diagram 

![uml.drawio.png](assets%2Fimages%2Fuml.drawio.png)

## Deployment

The API can be deployed using Docker. Here's how to build and run the Docker image.

### Build:

```bash
$ docker build -t 1mlet .
```

### Run:

- With port exposed
```bash
$docker run -d -p 8000:8000 --name c_1mlet 1mlet
```

- Without port exposed
```bash
$docker run -d --name c_1mlet 1mlet
```

- With Docker Compose (includes database integration):
```bash
$ docker-compose up -d
```

## Contributors (Group 43)
- Bruno Machado Corte Real
- Pedro Henrique Romaoli Garcia
- Rodrigo Santili Sgarioni
- Daniela Schutt Bogorny
- Rafael Anizio Gonçalves
