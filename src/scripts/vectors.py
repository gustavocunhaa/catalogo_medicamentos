import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import psycopg2 as pgsql
import pandas as pd
from transformers import AutoTokenizer  
from transformers import AutoModel
import torch


class VectorDatabase():

    def __init__(self, user, password, host, port, database, model_id):

        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.model_id = model_id

    def make_engine(self):
        url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        con = create_engine(url)
        return con
    
    def read_data(self, con):
        query_infos = """
            SELECT
                f.medicamento_id,
                CONCAT(clf.produto, ' ', clf.principio_ativo, ' ', 
                    clf.tipo, ' ', clf.categoria, ' ', 
                    clf.classe_terapeutica, ' ', clf.especialidade, ' ', 
                    clf.fabricante) as descricao
            FROM fat_produto f
            INNER JOIN dim_classificacao_produto clf
                on f.medicamento_id = clf.medicamento_id
            LEFT JOIN dim_vetores vt
                on f.medicamento_id = vt.medicamento_id
            WHERE
                1=1
                and f.deleted_at is null
                and vt.vetor is null
        """
        df = pd.read_sql(query_infos, con)
        print(f"Read data... {df.shape}")
        return df
    
    def make_vectors(self, text):
        model_id = self.model_id
        
        tokenizer = AutoTokenizer.from_pretrained(model_id, do_lower_case=False, clean_up_tokenization_spaces=True)
        model = AutoModel.from_pretrained(model_id)
        
        input_ids = tokenizer.encode(f'{text}', return_tensors='pt')
        with torch.no_grad():
            outs = model(input_ids)
            encoded = outs[0][0, 1:-1]  # Ignore [CLS] and [SEP] special tokens
        vetor = encoded.mean(dim=0).detach().numpy() # Mean of vectors
        
        return list(vetor)
    
    def exec_query(self, query):
        conn = pgsql.connect(database = self.database, 
                user = self.user, 
                host = self.host,
                password = self.password,
                port = self.port)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()        

    def save_vectors(self, medicamento_id, vetor):
        sql_insert = f""" 
        INSERT INTO dim_vetores(medicamento_id, vetor) VALUES({medicamento_id}, '{vetor}');
        """
        self.exec_query(sql_insert)
        print(f"Save value for medicamento_id {medicamento_id}")

    def run(self):
        con = self.make_engine()
        df = self.read_data(con)
        for n in range(0, len(df)):
            medicamento_id = df['medicamento_id'][n]
            text = [df['descricao'][n]]
            print(f"Process for medicamento_id {medicamento_id}")
            output = self.make_vectors(text)
            self.save_vectors(medicamento_id, output)
        

load_dotenv() # carrega credenciais

VectorDatabase(
    user=os.environ['user'],
    password=os.environ['password'],
    host=os.environ['host'],
    port=os.environ['port'],
    database=os.environ['database'],
    model_id = "neuralmind/bert-base-portuguese-cased"
).run()
