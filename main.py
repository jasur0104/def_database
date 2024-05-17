import psycopg2

db_name = 'n47'
password = '1'
host = 'localhost'
port = 5432
user = 'postgres'

with psycopg2.connect(dbname=db_name,
                      user=user,
                      password=password,
                      host=host,
                      port=port) as conn:
    with conn.cursor() as cur:
        def menyu():
            print("assalomu alykum xush kelibssz")
            print("table yaratamiz ")
            return create_table_query()

        def create_table_query():
            create_table="""
            CREATE TABLE IF NOT EXISTS productss(
            id serial PRIMARY KEY,
            name varchar(255) not null,
            image varchar(255) not null,
            create_at timestamp not null default CURRENT_TIMESTAMP,
            update_at timestamp not null default CURRENT_TIMESTAMP);
            """
            cur.execute(create_table)
            conn.commit()
            return insert_data_query()
        def alter_table_query():
            alter_table="""alter table productss
            add column is_liked boolean not null default FALSE; """
            cur.execute(alter_table)
            conn.commit()
            return create_table_query()
        def insert_data_query(data):
            name=input("name:")
            image=input("image:")
            is_liked=input("is_liked:")
            insert_data="""insert into productss(name, image,is_liked) values (%s,%s,%s,%s)"""
            cur.execute(insert_data,(name,image,is_liked))
            conn.commit()
            return select_data_query()

        def select_data_query():
            select_data="""select * from productss;"""
            cur.execute(select_data)
            return cur.fetchall()
        #bu bizga hozi hamma malumotlarini olib beradi
        def select_all_data_query():
            select_all="""select * from productss where id=1; """
            cur.execute(select_all)
            return cur.fetchall()
        #bu bizga id buyicha bitta malumot qaytaradi
        def update_table_query():
          update_table = """update productss set name = %s,image = %s where id = %s"""
          name = input('Enter title: ')
          image = input('Enter Image : ')
          _id = int(input('ID : '))
          cur.execute(update_table, (title, image, _id))
          conn.commit()
          return select_all_data_query()

        def delete_table_query():
            _id = int(input('ID : '))
            delete_data="""delete from categories where id = %s;"""
            data = (_id,)
            cur.execute(delete_data, data)
            conn.commit()
            return select_all_data_query()
        def create_table():
            table="""create table employee(
            id serial PRIMARY KEY,
            name varchar(255) not null,
            price float not null ,
            product_id int references products(id)
            );
            """
            cur.execute(table)
            conn.commit()
            return f'employe table yaratildi'

if __name__ == '__main__':
    create_table()
