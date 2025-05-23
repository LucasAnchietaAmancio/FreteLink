import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
from database.data import conectar

# Carregar variáveis de ambiente apenas uma vez
load_dotenv()

def enviar_email():
    conn = conectar()
    query = "SELECT * FROM serialcode WHERE status <> 'inativo'"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    email = os.getenv('EMAIL')
    senha = os.getenv('SENHA')

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = email
    password = senha

    mensagem = MIMEMultipart()
    mensagem['From'] = username
    mensagem['To'] = email
    mensagem['Subject'] = 'Código de acesso'

    corpo = f'Olá, seguem as seguintes credenciais válidas:\n{rows}'
    mensagem.attach(MIMEText(corpo, 'plain'))

    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        
        texto = mensagem.as_string()
        server.sendmail(username, email, texto)  # Aqui é variável email
        
        print('E-mail enviado com sucesso!')

    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')

    finally:
        if server:
            try:
                server.quit()
            except Exception as e:
                print(f'Erro ao fechar a conexão SMTP: {e}')
