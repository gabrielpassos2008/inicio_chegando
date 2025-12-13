import sqlite3 
from datetime import datetime
def verificar_email(email):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_verificar_email = ('''
        SELECT email
        FROM usuarios
        WHERE email = ?
        ''')
        cursor.execute(sql_verificar_email,(email,))
        resultado = cursor.fetchone()
        if resultado:
            return True
        else:
            return False
        
def cadastrar_usuario(nome,email,senha,data_nascimento,telefone):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        sql_cadastrar_usuario = ('''
        INSERT INTO usuarios (nome,email,senha,data_nascimento,telefone)
        VALUES(?,?,?,?,?)
        ''')
        conn.execute(sql_cadastrar_usuario,(nome,email,senha,data_nascimento,telefone))
        return True

def cadastrar_pedido_guincho(placa,endereco_origem,endereco_final):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        data = datetime.now()
        sql_cadastrar_pedido  = ('''
        INSERT INTO solicitacao_de_guincho (placa_carro,local_de_origem,local_de_destino,data_hora)
        VALUES(?,?,?,?)
        ''')
        conn.execute(sql_cadastrar_pedido,(placa,endereco_origem,endereco_final,data))
        return True
    
def pesquisar_login(email,senha):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_pesquisar_login = ('''
        SELECT id
        FROM usuarios
        WHERE email = ? AND senha = ?
        ''') 
        cursor.execute(sql_pesquisar_login,(email,senha))
        resultado = cursor.fetchone()
        return resultado
    

print(pesquisar_login('123@gmail','123'))
def dados_perfil(email):
    with sqlite3.connect('banco_chegando_pi.db') as conn:
        cursor = conn.cursor()
        sql_dados_perfil = ('''
        SELECT nome,email,data_nascimento,telefone
        FROM usuarios
        where email = ?
        ''')
        cursor.execute(sql_dados_perfil,(email,))
        resultado = cursor.fetchall()
        return resultado 


        
