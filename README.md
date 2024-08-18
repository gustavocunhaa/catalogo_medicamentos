# Drug Catalog
Projeto de modelagem de uma base de medicamentos para utilização em catálogos, bases de dados estruturadas, etc.

O objetivo é ter uma base que retorne informações funcionais, mas também que apresente bons agrupamentos dos produtos listados. Não só a base de dados será construída, mas uma API para consumo dessas informações.

<div style="display: inline_block"><br>
  <img align="center" alt="python" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
  <img align="center" alt="aws" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/amazonwebservices/amazonwebservices-original-wordmark.svg">
  <img align="center" alt="s3" height="50" width="60" src="https://cdn.worldvectorlogo.com/logos/amazon-s3-simple-storage-service.svg">
  <img align="center" alt="pgsql" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/postgresql/postgresql-original.svg">
  <img align="center" alt="hugginface" height="50" width="60" src="https://cdn.worldvectorlogo.com/logos/huggingface-2.svg">
  <img align="center" alt="pytorch" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytorch/pytorch-original.svg">
  <img align="center" alt="sklearn" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg"> 
  <img align="center" alt="fastapi" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/fastapi/fastapi-original-wordmark.svg">
  <img align="center" alt="streamlit" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg"> 
</div>   

### Arquitetura do projeto

![projeto](docs/[GitHub]%20Arch%20-%20catalogo%20de%20medicamentos.jpg)

- Informações estruturadas sobre medicamentos
- Base de vetores para busca por similaridade de texto
- API para manipulação da base de produtos e utilização do sistema de recomendação

> Todas as credenciais necessárias para manipulação do banco devem estar no arquivo [.env](example.env)

## Vetores

A base de vetores foi construída utilizando os embedings do modelo [BERTimbau](https://huggingface.co/neuralmind/bert-base-portuguese-cased) e utilizando o [pgvector](https://github.com/pgvector/pgvector) para armazenrar e manipular os vetores.


## Sistema de recomendação

O sistema tem 3 tipos diferentes de recomendações, onde são recomendados produtos com base no input inicial textual.

![recomendacao](docs/[GitHub]%20Arch%20-%20catalogo%20de%20medicamentos_%20recomendacao.jpg)
