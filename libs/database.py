import sqlite3

def create_table_if_not_exists():
    try:
        with sqlite3.connect('Carros.db') as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Carros (id INTEGER PRIMARY KEY AUTOINCREMENT, marca TEXT, modelo TEXT, ano INTEGER)')
    except sqlite3.Error as e:
        print(f'Ocorreu um erro ao tentar criar a tabela: {e}')

def execute_insert(carro):
    create_table_if_not_exists()
    try:
        with sqlite3.connect('Carros.db') as conn:
            cursor = conn.cursor()
            query = 'INSERT INTO Carros (marca, modelo, ano) VALUES (?, ?, ?)'
            cursor.execute(query, (carro['marca'], carro['modelo'], carro['ano']))
            conn.commit()
        return 'Carro cadastrado com sucesso.'
    except sqlite3.Error as e:
        return f'Ocorreu um erro ao tentar inserir os dados: {e}'
        
def execute_select():
    create_table_if_not_exists()
    try:
        with sqlite3.connect('Carros.db') as conn:
            cursor = conn.cursor()
            query = 'SELECT * FROM Carros'
            cursor.execute(query)
            resultado = [{'id': carro[0], 'marca': carro[1], 'modelo': carro[2], 'ano': carro[3]} for carro in cursor.fetchall()]
            return [resultado, 'Lista de carros.']
    except sqlite3.Error as e:
        return [[], f'Ocorreu um erro ao tentar consultar os dados: {e}']