import sqlite3
import os
from sqlite3 import Error
from pprint import pprint

from faker import Faker
from random import choice

persistent = False


def create_db():
    db_file = "sqlite_from_python.db"
    if not os.path.isfile(db_file):
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            conn.close()
    else:
        print("DB already exists")


def create_table(conn, cursor, table_name, table_headers):
    """

    :param cursor: connection cursor
    :param table_name: name of table to create in database
    :param table_headers: headers names as list
    :return:
    """
    strigified_data = ",".join(table_headers)
    cursor.execute(f"CREATE TABLE {table_name} ({strigified_data})")
    conn.commit()


def insert_row(conn, cursor, table_name, data):
    strigified_data = ",".join([f"{d}" if str(d).isnumeric() else f"'{d}'" for d in data])
    cursor.execute(f"INSERT INTO {table_name} VALUES ({strigified_data})")
    conn.commit()


if __name__ == '__main__':
    create_db()
    conn = sqlite3.connect("sqlite_from_python.db")
    curs = conn.cursor()
    fake = Faker()

    try:
        create_table(conn,
                     curs,
                     "stocks",
                     ["date_text","trans_text","symbol_text","qty_real","price_real"])
    except sqlite3.OperationalError:
        print("Table already created")

    insert_row(conn,
               curs,
               "stocks",
               ['2006-01-05','BUY','RHAT',100,35.14])

    for _ in range(0, 10):
        data = [
            fake.date_between(start_date='today', end_date='+30y'),
            fake.random.choice(["BUY", "SELL"]),
            fake.word(),
            fake.random_int(),
            fake.random_number()
        ]
        # print(data)
        insert_row(conn,
                   curs,
                   "stocks",
                   data)

    print("selecting all")
    dane = curs.execute("Select * from stocks ")
    pprint(dane.fetchall())

    print("selecting BUY")
    dane = curs.execute("Select * from stocks where trans_text = 'BUY'")
    pprint(dane.fetchall())

    print("selecting SELL")
    dane = curs.execute("Select * from stocks where trans_text = 'SELL'")
    pprint(dane.fetchall())


    if not persistent:
        os.remove("sqlite_from_python.db")

    conn.close()


