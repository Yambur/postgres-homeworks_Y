"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import os

password_sql = os.getenv('PASSWORD_SQL')

with psycopg2.connect(host='localhost', database='north', user='postgres', password=password_sql) as conn:
    with open('north_data/customers_data.csv', encoding='utf-8') as file:
        csv.field_size_limit(10 ** 8)
        reader = csv.reader(file)
        next(reader)
        with conn.cursor() as cur:
            for i in reader:
                try:
                    cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (i[0], i[1], i[2]))
                finally:
                    conn.commit()

    with open('north_data/employees_data.csv', encoding='utf-8') as file:
        csv.field_size_limit(10 ** 8)
        reader = csv.reader(file)
        next(reader)
        with conn.cursor() as cur:
            for i in reader:
                try:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                (i[0], i[1], i[2], i[3], i[4], i[5]))
                finally:
                    conn.commit()

    with open('north_data/orders_data.csv', encoding='utf-8') as file:
        csv.field_size_limit(10 ** 8)
        reader = csv.reader(file)
        next(reader)
        with conn.cursor() as cur:
            for i in reader:
                try:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                                (i[0], i[1], i[2], i[3], i[4]))
                finally:
                    conn.commit()
conn.close()
