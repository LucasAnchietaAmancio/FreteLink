import pandas as pd
from database.data import conectar

def exportar_notas(data_inicial, data_final, motorista, log_callback=None):
    conn = conectar()
    try:
        query = """
            SELECT DISTINCT
                n.id_note,
                n.data_emissao,
                n.data_consulta,
                n.numero_nota,
                n.valor,
                n.status,
                n.codigo_motorista,
                n.remetente,
                n.destinatario,
                m.nome AS nome_motorista,
                m.cpf AS cpf_motorista
            FROM notas n
            LEFT JOIN motoristas m ON m.id_motorista = n.motorista_id
            WHERE n.data_emissao BETWEEN %s AND %s
            AND m.nome = %s
        """

        cursor = conn.cursor()
        cursor.execute(query, (data_inicial, data_final, motorista))
        rows = cursor.fetchall()

        colunas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=colunas)

        if df.empty:
            mensagem = "Nenhum registro encontrado para os filtros informados."
            if log_callback:
                log_callback(mensagem)
            else:
                pass
            return

        caminho = rf"C:\NOTAS\notas_exportadas_{data_final}_{motorista}.xlsx"
        df.to_excel(caminho, index=False)
        mensagem = f"Exportação concluída: {caminho}"
        if log_callback:
            log_callback(mensagem)
        else:
            print(mensagem)  # fallback para console

    except Exception as e:
        mensagem = f"❌ Erro ao exportar notas: {e}"
        if log_callback:
            log_callback(mensagem)
        else:
            pass
        raise
    finally:
        conn.close()
