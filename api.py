import os
from dotenv import load_dotenv

import json
from fastapi import FastAPI
from transformers import AutoModel, AutoTokenizer
import torch

from src.api.schemas import BuscaProdutos, MontaVetor, DistanciaVetores, ColetaInfo, RecomendacaoPorId
from src.api.handler import DatabaseHandler
from src.api         import querys

app = FastAPI()
load_dotenv()
database_handler = DatabaseHandler(
    user=os.environ['user'],
    password=os.environ['password'],
    host=os.environ['host'],
    port=os.environ['port'],
    database=os.environ['database'],
)


@app.get("/")
async def root():
    return "API API for handling the product catalog. Try /docs"


@app.get("/list/", description="Retorna todos os IDs de produtos ativos")
async def get_lista_produtos():
    query = querys.list_ids()
    df = database_handler.exec_sql(query)
    response = df['medicamento_id'].tolist()
    return response


@app.post("/product/info/", description="Coleta as informações listadas de um produto")
async def coleta_informacoes(data: ColetaInfo):
    body = json.loads(data.model_dump_json())
    query = querys.collect_info(
        id_list=body['lista_ids'], 
        columns=body['atributos'])
    df = database_handler.exec_sql(query)
    response = df.to_json(orient='records')
    return response

@app.post("/product/find/", description="Busca um produto de acordo com o texto")
async def busca_produtos(data: BuscaProdutos):
    body = json.loads(data.model_dump_json())
    query = querys.find_product(body['busca'])
    df = database_handler.exec_sql(query)
    response = {
        "medicamento_id": str(df['medicamento_id'][0]),
        "descricao":      str(df['descricao'][0])
    }
    return response

@app.post("/makevector/", description="Endpoint para facilitar a criação de um novo vetor")
async def monta_vetorizacao(data: MontaVetor):
    body = json.loads(data.model_dump_json())
    text = str(body['texto'])

    model_id = 'neuralmind/bert-base-portuguese-cased'
    model = AutoModel.from_pretrained(model_id)
    
    tokenizer = AutoTokenizer.from_pretrained(model_id, do_lower_case=False, clean_up_tokenization_spaces=True)
    input_ids = tokenizer.encode(f'{text}', return_tensors='pt')
    
    with torch.no_grad():
        outs = model(input_ids)
        encoded = outs[0][0, 1:-1]  # Ignore [CLS] and [SEP] special tokens
    vetor = encoded.mean(dim=0).detach().numpy()
    response = str(list(vetor))
    return response

@app.post("/recommendation/find/", description="Faz a busca dos produtos mais semelhantes com base no texto")
async def recomendacao_vetorial(data: DistanciaVetores):
    body = json.loads(data.model_dump_json())
    query = querys.distance_vector(body['vetor'])
    df = database_handler.exec_sql(query)
    response = df['medicamento_id'].tolist()
    return response


@app.post("/recommendation/rule/", description="Faz a busca de protudos intercambiáveis")
async def recomenda_intercambiavel(data: RecomendacaoPorId):
    body = json.loads(data.model_dump_json())
    query_infos = querys.collect_info(
        id_list=[body['medicamento_id']], 
        columns=['tipo']
        )
    infos = database_handler.exec_sql(query_infos)
    
    query = querys.rule_find(
        medicamento_id=int(infos['medicamento_id'][0]),
        type=str(infos['tipo'][0])
        )
    df = database_handler.exec_sql(query)
    response = df['medicamento_id'].tolist()
    return response

@app.post("/recommendation/cluster/", description="Faz a busca de produtos com base no mesmo agrupamento de cluster")
async def recomenda_cluster(data: RecomendacaoPorId):
    body = json.loads(data.model_dump_json())
    query = querys.cluster_find(int(body['medicamento_id']))
    df = database_handler.exec_sql(query)
    response = df['medicamento_id'].to_list()
    return response