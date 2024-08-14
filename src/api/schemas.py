from pydantic import BaseModel

class ColetaInfo(BaseModel):
    lista_ids: list
    atributos: list

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "lista_ids": [1, 2, 3],
                    "atributos": ['produto', 
                                  'principio_ativo', 'tipo_produto',
                                  'fabricante',
                                  'especialidade', 'classe_terapeutica', 'categoria',
                                  'codigo_barras', 'tipo_receita']
                }
            ]
        }
    }
