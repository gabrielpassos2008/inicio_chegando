import sqlite3
from datetime import datetime
def criar_banco():
    conexao = sqlite3.connect('banco_chegando_pi.db')
    criar_tab_status(conexao)
    criar_tab_veiculo(conexao)
    criar_tab_usuarios(conexao)
    criar_tab_solicitacao_de_guincho(conexao)
   
#criação de tabela status
def criar_tab_status(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS status(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL
    );
    ''')
    #criação de tabela veiculo
def criar_tab_veiculo(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS veiculo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        modelo TEXT NOT NULL,
        cor TEXT NOT NULL,
        id_usuarios INTEGER,
        FOREIGN KEY(id_usuarios) REFERENCES usuarios(id)
    );
    ''')

#criação de tabela usuario
def criar_tab_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT  NULL,
        data_nascimento DATE NOT NULL,
        telefone TEXT,
        tipo INT DEFAULT 0,
        id_veiculo INTEGER,
        FOREIGN KEY(id_veiculo) REFERENCES veiculo(id)
    );
    ''')

#criação de tabela solicitacao_de_guincho
def criar_tab_solicitacao_de_guincho(conn):
    cursor = conn.cursor()
    print("""
CREATE TABLE IF NOT EXISTS solicitacao_de_guincho(
    ...
)
""")
    cursor.execute('''
CREATE TABLE IF NOT EXISTS solicitacao_de_guincho(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    placa_carro TEXT NOT NULL,
    local_de_origem TEXT NOT NULL,
    local_de_destino TEXT NOT NULL,
    status INT DEFAULT 0,
    data_hora DATETIME,
    id_usuarios INTEGER,
    id_status INTEGER,
    FOREIGN KEY(id_usuarios) REFERENCES usuarios(id),    
    FOREIGN KEY(id_status) REFERENCES status(id)
);
    ''')

criar_banco()

