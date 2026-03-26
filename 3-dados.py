import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('titulo.bd')
cursor = conexao.cursor()

# 2 - Inserir dados
cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES ('Sonic', 2020, 8)
    """
)
conexao.commit()
conexao.close()
print("Dados inserido na tabela")
