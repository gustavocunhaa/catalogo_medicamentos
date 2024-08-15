def list_ids():
    query = f''' 
        SELECT 
            medicamento_id
        FROM fat_produto
        WHERE deleted_at is null
    '''
    return query

def collect_info(id_list: list, columns: list):
    ensure_list = ['produto', 
                   'principio_ativo', 
                   'tipo',
                   'fabricante',
                   'especialidade',
                   'classe_terapeutica',
                   'categoria',
                   'codigo_barras',
                   'tipo_receita']
    
    format_list = []
    for info in columns:
        if info not in ensure_list:
            return print(f"Query com parametros invalidos. Coluna não está na lista. Lista {ensure_list}")
        elif info in ('codigo_barras', 'tipo_receita'):
            format_list.append(f'reg.{info}')
        else:
            format_list.append(f'clf.{info}')

    query = f''' 
        SELECT 
            f.medicamento_id,
            {", ".join(format_list)}
        FROM fat_produto f
        INNER JOIN dim_classificacao_produto clf ON clf.medicamento_id = f.medicamento_id
        INNER JOIN dim_registro_regulatrio reg ON reg.medicamento_id = f.medicamento_id
        WHERE 
            1=1
            and f.medicamento_id in ({', '.join(map(str, id_list))})
            and f.deleted_at is null
    '''
    return query

def find_product(text_find: str):
    query = f""" 
    SELECT
        medicamento_id,
        CONCAT(produto, ' ', principio_ativo, ' ', tipo, ' ', categoria, ' ', classe_terapeutica, ' ', especialidade, ' ', fabricante)  as descricao 
    FROM dim_classificacao_produto
    WHERE 
        CONCAT(produto, ' ', principio_ativo, ' ', tipo, ' ', categoria, ' ', classe_terapeutica, ' ', especialidade, ' ', fabricante) 
        ILIKE '%%{text_find}%%'
    LIMIT 1;
    """
    return query


# Recommendation section
LIMIT = 2

def distance_vector(vetor: str):
    query = f"""
        SELECT 
            medicamento_id 
        FROM dim_vetores
        ORDER BY vetor <=> '{vetor}'
        LIMIT {LIMIT};
    """
    return query

def rule_find(medicamento_id: int, type: str):
    if type in ("Genérico", "Referência", "Similar Intercambiável"):
        query = f""" 
            SELECT
                f.medicamento_id
            FROM fat_produto f
            INNER JOIN dim_classificacao_produto clf on f.medicamento_id = clf.medicamento_id
            INNER JOIN dim_preco pr on f.medicamento_id = pr.medicamento_id
            WHERE
                1=1
                and f.deleted_at is NULL
                and clf.tipo = 'Genérico'
                and clf.principio_ativo = (SELECT principio_ativo FROM dim_classificacao_produto WHERE medicamento_id = {medicamento_id})
                and f.medicamento_id <> {medicamento_id}
            GROUP BY f.medicamento_id
            ORDER BY AVG(pr.pmc_valor)
            LIMIT {LIMIT};
        """
    else:
        query = f""" 
            SELECT
                f.medicamento_id
            FROM fat_produto f
            INNER JOIN dim_classificacao_produto clf on f.medicamento_id = clf.medicamento_id
            INNER JOIN dim_preco pr on f.medicamento_id = pr.medicamento_id
            WHERE
                1=1
                and f.deleted_at is NULL
                and clf.tipo = '{type}'
                and clf.principio_ativo = (SELECT principio_ativo FROM dim_classificacao_produto WHERE medicamento_id = {medicamento_id})
                and f.medicamento_id <> {medicamento_id}
            GROUP BY f.medicamento_id
            ORDER BY AVG(pr.pmc_valor)
            LIMIT {LIMIT};
        """
    return query
        
def cluster_find(medicamento_id: int):
    query = f""" 
        SELECT
            medicamento_id
        FROM dim_cluster
        WHERE cluster = (SELECT cluster FROM dim_cluster WHERE medicamento_id = {medicamento_id})
        ORDER BY RANDOM()
        LIMIT {LIMIT};
    """
    return query