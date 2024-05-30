import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()
db_params = {
    'database': os.getenv('database'),
    'user': os.getenv('user'),
    'password': os.getenv('password'),
    'host': os.getenv('host'),
    'port': os.getenv('port'),
}

class CAntextConnectDB:
    def __init__(self, db_params: dict):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        self.cur = self.conn.cursor()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.conn.rollback()
        if self.conn:
            self.cur.close()
            self.conn.close()

    def commit(self):
        self.conn.commit()


def table():
    with CAntextConnectDB(db_params) as db:
        crete_table="""create table if not exists productss(
           id serial primary key,
           name varchar(255),
           price int)"""
        db.cur.execute(crete_table)
        db.commit()
        print('table yaratildi')
table()


class Product:
    def __init__(self, name,price:int):
        self.name = name
        self.price = price

    def insert(self):
        with CAntextConnectDB(db_params) as db:
            insert_into_car = """INSERT INTO productss(name,price)
            values (%s,%s);
            """
            db.cur.execute(insert_into_car, (self.name,self.price))
            db.commit()
            print('malumotlar qushildi')
product1=Product('a32',1000)
product2=Product('iphone12',2300)
product3=Product('muslatkich',4500)
product1.insert()
product2.insert()
product3.insert()
def select_products():
    with CAntextConnectDB(db_params) as db:
        select="""select * from productss;
        """
        db.cur.execute(select)
        productss=db.cur.fetchall()
        for product in productss:
            print(product)
select_products()