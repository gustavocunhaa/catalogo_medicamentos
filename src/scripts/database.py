import os
import argparse
from dotenv import load_dotenv

import awswrangler as wr
from sqlalchemy import create_engine

class InsertData():

    def __init__(self, user, password, host, port, database, partition, s3_file):

        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.partition = partition
        self.s3_file = s3_file

    def make_engine(self):
        url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        con = create_engine(url)
        return con
    
    def read_s3(self):
        file = f"s3://catalogo-medicamentos/{self.partition}/{self.s3_file}.parquet"
        df = wr.s3.read_parquet(file)
        return df
    
    def create_table(self):
        con = self.make_engine()
        df_table = self.read_s3().sort_values(by="medicamento_id")
        df_table.to_sql(self.s3_file, con, if_exists="replace", index=False)


parser = argparse.ArgumentParser(description="Insert Data")
parser.add_argument("--partition", required=True)
parser.add_argument("--file_name", required=True)
args = parser.parse_args()

load_dotenv()

InsertData(
    user=os.environ['user'],
    password=os.environ['password'],
    host=os.environ['host'],
    port=os.environ['port'],
    database=os.environ['database'],
    partition=args.partition,
    s3_file=args.file_name
).create_table()