import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import psycopg2 as pgsql
import pandas as pd
import requests


class VectorDatabase():

    def __init__(self, user, password, host, port, database, model_id, hf_token):

        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.model_id = model_id
        self.hf_token = hf_token

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
            WHERE
                1=1
                and f.deleted_at is null
        """
        df = pd.read_sql(query_infos, con)
        return df
    
    def inference(self, texts):
        api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{self.model_id}"
        headers = {"Authorization": f"Bearer {self.hf_token}"}
        response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
        return response.json()

    def make_vectors(self):
        con = self.make_engine()
        df = self.read_data(con)
        output = self.inference(df['descricao'].tolist())
        vector_list = []
        for i in range(0, len(output)):
            vector_list.append(output[i][0][0]) # collect CLS token
        df['vetor'] = vector_list
        return df

    def save_vectors(self, df):
        conn = pgsql.connect(database = self.database, 
                     user = self.user, 
                     host = self.host,
                     password = self.password,
                     port = self.port)

        for n in range(0, len(df)):
            sql_insert = f""" 
            INSERT INTO dim_vetores(medicamento_id, vetor) VALUES({df['medicamento_id'][n]}, '{df['vetor'][n]}');
            """
            cur = conn.cursor()
            cur.execute(sql_insert)
            conn.commit()
            cur.close()
            conn.close()

    def run(self):
        vectors_df = self.make_vectors()
        self.save_vectors(vectors_df)
        

load_dotenv()

VectorDatabase(
    user=os.environ['user'],
    password=os.environ['password'],
    host=os.environ['host'],
    port=os.environ['port'],
    database=os.environ['database'],
    model_id = "neuralmind/bert-base-portuguese-cased",
    hf_token = os.environ['hf_token']
).run()
