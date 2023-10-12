import pandas as pd
import sqlite3

nome_arquivo_csv = 'cidades ECOnnect  - global_horizontal_means_sedes-munic (1).csv'
nome_banco_de_dados = 'econnectdb.sqlite'


df = pd.read_csv(nome_arquivo_csv)


tabela = 'sua_tabela'

try:
    conn = sqlite3.connect(nome_banco_de_dados)
    cursor = conn.cursor()

    cursor.execute(f"CREATE TABLE IF NOT EXISTS {tabela} (NAME TEXT, STATE TEXT, ANNUAL REAL)")

    for _, row in df.iterrows():
        name = row['NAME']
        state = row['STATE']
        annual = row['ANNUAL']

        inserir_dados = f"INSERT INTO {tabela} (NAME, STATE, ANNUAL) VALUES (?, ?, ?)"

        valores = (name, state, annual)

        cursor.execute(inserir_dados, valores)

    conn.commit()

    print("Dados do CSV inseridos no banco de dados SQLite com sucesso!")

except sqlite3.Error as err:
    print(f"Erro: {err}")

finally:
    cursor.close()
    conn.close()
