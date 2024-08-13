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
    
    def inference(self, texts):
        api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{self.model_id}"
        headers = {"Authorization": f"Bearer {self.hf_token}"}
        print("Making inference...")
        response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
        return response.json()

    def make_vectors(self, list_text):
        output = self.inference(list_text)
        print(output)
        return output[0][0][0] # collect only CLS token
    
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
            text_list = [df['descricao'][n]]
            print(f"Process for medicamento_id {medicamento_id}")
            output = self.make_vectors(text_list)
            self.save_vectors(medicamento_id, output)
        


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
