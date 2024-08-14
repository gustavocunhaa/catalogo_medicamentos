from pydantic import BaseModel

class ColetaInfo(BaseModel):
    lista_ids: list
    atributos: list

