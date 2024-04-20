# Autor: João Pedro Rodrigues Tenório
# Matrícula: 1810518
# Disciplina: Programação Funcional
# Avaliação: AV2

import os
import mysql.connector

os.system('cls')

db = (lambda: mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="joaotenorio"
))()

cursor = (lambda: db.cursor())()

execute = (lambda query: cursor.execute(query))

drop_tables = (lambda tables: [execute(f"DROP TABLE IF EXISTS {table}") for table in tables])
drop_tables(["USERS", "VIDEOGAMES", "GAMES", "COMPANY"])

execute("""
CREATE TABLE USERS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    id_console INT
)
""")
execute("""
CREATE TABLE VIDEOGAMES (
    id_console INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    id_company INT,
    release_date DATE
)
""")
execute("""
CREATE TABLE GAMES (
    id_game INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    release_date DATE,
    id_console INT
)
""")
execute("""
CREATE TABLE COMPANY (
    id_company INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255)
)
""")

insert_into = (lambda table, values: execute(f"INSERT INTO {table} VALUES ({', '.join(values)})"))
delete_from = (lambda table, condition: execute(f"DELETE FROM {table} WHERE {condition}"))
select_from = (lambda table, condition: execute(f"SELECT * FROM {table} WHERE {condition}"))

insert_into("USERS", ["NULL", "'John Doe'", "'USA'", "1"])
insert_into("VIDEOGAMES", ["NULL", "'Game Console'", "1", "'2022-01-01'"])
insert_into("GAMES", ["NULL", "'Super Game'", "'Adventure'", "'2022-02-01'", "1"])
insert_into("COMPANY", ["NULL", "'Game Company'", "'USA'"])

db.commit()

print_data = (lambda tables: [select_from(table, "1=1") or print(f"Data from {table}:") or [print(row) for row in cursor] for table in tables])
print_data(["USERS", "VIDEOGAMES", "GAMES", "COMPANY"])

db.close()