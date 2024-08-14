# Drug Catalog
Projeto de modelagem de uma base de medicamentos para utilização em catálogos, bases de dados estruturadas, etc.

O objetivo é ter uma base que retorne informações funcionais, mas também que apresente bons agrupamentos dos produtos listados. Não só a base de dados será construída, mas uma API para consumo dessas informações.

### Arquitetura do projeto

![projeto](docs/[GitHub]%20Arch%20-%20catalogo%20de%20medicamentos.jpg)

- Informações estruturadas sobre medicamentos
- Base de vetores para busca por similaridade de texto
- API para manipulação da base de produtos e utilização do sistema de recomendação

> Todas as credenciais necessárias para manipulação do banco devem estar no arquivo [.env](example.env)

## Vetores

A base de vetores foi construída utilizando os embedings do modelo [BERTimbau](https://huggingface.co/neuralmind/bert-base-portuguese-cased) e utilizando o [pgvector](https://github.com/pgvector/pgvector) para armazenrar e manipular os vetores.