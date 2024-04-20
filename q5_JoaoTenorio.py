# Autor: João Pedro Rodrigues Tenório
# Matrícula: 1810518
# Disciplina: Programação Funcional
# Avaliação: AV2

# Arquivo q3_JoaoTenorio.py foi escolhido para essa questão.

from flask import Flask, request, jsonify
import mysql.connector
import bcrypt

app = Flask(__name__)

db = (lambda: mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="joaotenorio"
))()

cursor = (lambda: db.cursor())()

execute = lambda query: cursor.execute(query)

drop_tables = lambda tables: [execute(f"DROP TABLE IF EXISTS {table}") for table in tables]
drop_tables(["USERS", "VIDEOGAMES", "GAMES", "COMPANY"])

# Professor não sei se era o ideal, mas na criação do usuário eu criei junto dos outros o password_hash
execute("""
CREATE TABLE USERS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(255),
    id_console INT,
    password_hash VARBINARY(255)
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

# Peguei essa função da documentação deles e adptei para lambda
hash_password = lambda password: bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
get_password_hash = lambda: hash_password("samuel").decode()
insert_into = lambda table, values: execute(f"INSERT INTO {table} VALUES ({', '.join(values)})")
insert_into("USERS", ["NULL", "'John Doe'", "'USA'", "1", f"'{get_password_hash()}'"])

db.commit()

@app.route('/data', methods=['GET'])
def print_data():
    get_tables = lambda: ["USERS", "VIDEOGAMES", "GAMES", "COMPANY"]
    select_from = lambda table: execute(f"SELECT * FROM {table} WHERE 1=1") or cursor.fetchall()
    get_data = lambda: [{table: select_from(table)} for table in get_tables()]
    return jsonify(get_data())

if __name__ == '__main__':
    app.run(debug=True)