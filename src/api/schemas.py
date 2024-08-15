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

class BuscaProdutos(BaseModel):
    busca: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "busca": "Losartana"
                }
            ]
        }
    }

class MontaVetor(BaseModel):
    texto: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "texto": "Hipovas Besilato De Anlodipino + Losartana Potássica Genérico Anti-Hipertensivo Antagonistas Da Angiotensina Ii Associados A Antagonistas Do Cálcio Cardiologia Nova Química"
                }
            ]
        }
    }

class DistanciaVetores(BaseModel):
    vetor: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "vetor": ""}
            ]
        }
    }
