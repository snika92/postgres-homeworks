"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with open("north_data/customers_data.csv", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    list_of_lines = []
    for line in reader:
        list_of_lines.append((line['customer_id'], line['company_name'], line['contact_name']))

for line in list_of_lines:
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', line)
    conn.close()

with open("north_data/employees_data.csv", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    list_of_lines = []
    for line in reader:
        list_of_lines.append((line['employee_id'], line['first_name'], line['last_name'], line['title'],
                              line['birth_date'], line['notes']))

for line in list_of_lines:
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', line)
    conn.close()

with open("north_data/orders_data.csv", encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    list_of_lines = []
    for line in reader:
        list_of_lines.append((line['order_id'], line['customer_id'], line['employee_id'], line['order_date'],
                              line['ship_city']))

for line in list_of_lines:
    with psycopg2.connect(host='localhost', database='north', user='postgres', password='12345') as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', line)
    conn.close()
