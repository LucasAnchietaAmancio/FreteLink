from database.data import conectar
from datetime import datetime
import random
import string
from .enviar_serial import enviar_email

def gerar_serial(tamanho=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=tamanho))

def validar_licenca(serial):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM serialcode WHERE serial_validacao = %s AND status = 'ativo'", (serial,))
    row = cursor.fetchone()

    if row:
        print('Serial encontrada e válida')

        cursor.execute("UPDATE serialcode SET status = 'inativo' WHERE serial_validacao = %s", (serial,))

        nova_serial = gerar_serial()
        cursor.execute("INSERT INTO serialcode (serial_validacao, status) VALUES (%s, 'ativo')", (nova_serial,))

        conn.commit()
        conn.close()

        # Aqui registra a validação
        registrar_validacao()
        enviar_email()

        return True
    else:
        print('Serial inválida ou inativa')
        conn.close()
        return False

def precisa_validar_licenca():
    hoje = datetime.today().date()

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT data_validacao FROM licenca_validada ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()

    conn.close()

    if not resultado:
        return True

    data_validacao = resultado['data_validacao']

    if hoje.day == 2:
        return data_validacao != hoje
    else:
        return not (data_validacao.month == hoje.month and data_validacao.year == hoje.year)

def registrar_validacao():
    conn = conectar()
    cursor = conn.cursor()

    hoje = datetime.today().date()

    cursor.execute("INSERT INTO licenca_validada (data_validacao) VALUES (%s)", (hoje,))
    conn.commit()
    conn.close()

def verifica_expiracao():
    hoje = datetime.today().date()
    return hoje.day == 2
