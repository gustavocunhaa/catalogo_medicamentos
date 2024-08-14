import os
from dotenv import load_dotenv

import json
from fastapi import FastAPI
from src.api.schemas import ColetaInfo
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


@app.post("/infocollect/", description="Coleta as informações listadas de um produto")
async def coleta_informacoes(data: ColetaInfo):
    body = json.loads(data.model_dump_json())
    query = querys.collect_info(
        id_list=body['lista_ids'], 
        columns=body['atributos'])
    df = database_handler.exec_sql(query)
    response = df.to_json(orient='records')
    return response


