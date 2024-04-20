# Autor: João Pedro Rodrigues Tenório
# Matrícula: 1810518
# Disciplina: Programação Funcional
# Avaliação: AV2

import os
from q3_JoaoTenorio import execute, cursor, db

os.system('cls')

generate_inner_join = lambda tables, on_conditions: tables[0] + "".join(
    [" INNER JOIN " + tables[i] + " ON " + on_conditions[i-1] for i in range(1, len(tables))]
)

tables = lambda: ["GAMES", "VIDEOGAMES", "COMPANY"]
on_conditions = lambda: ["GAMES.id_console = VIDEOGAMES.id_console", "VIDEOGAMES.id_company = COMPANY.id_company"]
attributes = lambda: ["GAMES.title", "COMPANY.name"]
inner_join_query = lambda: generate_inner_join(tables(), on_conditions())
select_query = lambda: f"SELECT {', '.join(attributes())} FROM {inner_join_query()}"

print("Professor estou só debugando kkk: ", select_query())
execute(select_query())

db.close()