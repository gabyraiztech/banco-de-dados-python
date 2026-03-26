import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('titulo.bd')

# 2 - Criando o cursor
cursor = conexao.cursor()

# 3 - Criando a tabela (Ajustado o PRIMARY KEY)
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

# 4 - Salva as alterações
#conexao.commit()

# 5 - Fecha conexão
conexao.close()
print("Tabela 'filmes' criada com sucesso!")