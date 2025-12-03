import sqlite3
from datetime import datetime
def criar_banco():
    conexao = sqlite3.connect('banco_chegando_pi.db')
    criar_tab_usarios(conexao)
    criar_tab_veiculo(conexao)
    criar_tab_solicitacao_de_guincho(conexao)
#criação de tabela seguradora
def criar_tab_usarios(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT  NULL,
        tipo INT DEFAULT 0
    );
    ''')

def criar_tab_veiculo(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS veiculos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        placa TEXT NOT NULL,
        modelo TEXT NOT NULL,
        cor TEXT NOT NULL,
        id_usuarios INTEGER,
        FOREIGN KEY(id_usuarios) REFERENCES usuarios(id)
    );
    ''')
    
#criação de tabela solicitacao_de_guincho
def criar_tab_solicitacao_de_guincho(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS solicitacao_de_guincho(
        id  INTEGER PRIMARY KEY  AUTOINCREMENT,
        placa_carro TEXT NOT NULL,               
        local_de_origem TEXT NOT NULL,
        local_de_destino TEXT NOT NULL,           
        status INT DEFAULT 0,
        data_hora DATETIME,
        id_usuarios INTEGER,
        FOREIGN KEY(id_usuarios) REFERENCES usuarios(id)                 
    );
    ''')

criar_banco()

