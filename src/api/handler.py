from sqlalchemy import create_engine
from pandas     import read_sql

class DatabaseHandler():

    def __init__(self, user, password, host, port, database):

        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

        self.conn = self.make_engine()

    def make_engine(self):
        url = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        con = create_engine(url)
        return con
    
    def exec_sql(self, query: str):
        df = read_sql(query, self.conn)
        return df