import pymysql
from datetime import datetime
from decimal import Decimal
from PySide6.QtWidgets import QMessageBox

def conectar(log_callback=None):
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='lucasapp',
            password='123456',
            database='sistema_cte',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return conexao
    except pymysql.MySQLError as err:
        log_callback("Erro de Conexão", f"Erro ao conectar ao MySQL:\n{err}")
        return None

def inserir_nota(conn, dados, log_callback=None):
    try:
        data_emissao = datetime.strptime(dados['data_emissao'], '%d/%m/%Y %H:%M')

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO notas (
                    data_emissao, data_consulta, numero_nota, valor, status,
                    codigo_motorista, remetente, destinatario
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                data_emissao,
                datetime.today().date(),
                dados['numero_data'],
                Decimal(dados['valor'].replace('R$', '').replace('.', '').replace(',', '.')),
                "Autorizada",
                dados['codigo_motorista'],
                dados['remetente'],
                dados['destinatario'],
            ))
            conn.commit()
            log_callback( "Inserção", "Nota inserida com sucesso.")
    except pymysql.MySQLError as err:
        log_callback("Erro de Inserção", f"Erro ao inserir nota:\n{err}")

def cadastrar_motorista(conn, rntrc, nome, cpf, data_nascimento_str, log_callback=None):
    try:
        data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO motoristas (rntrc, nome, cpf, data_nascimento)
                VALUES (%s, %s, %s, %s)
            """, (rntrc, nome, cpf, data_nascimento))
            conn.commit()
            
    except pymysql.MySQLError as err:
        log_callback("Erro de Cadastro", f"Erro ao cadastrar motorista:\n{err}")

def consulta_motorista(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT nome FROM motoristas")
        motorista = cursor.fetchall()
        return motorista
