📦 Automação CTe
Automação completa para a coleta, processamento e armazenamento de informações de Conhecimento de Transporte Eletrônico (CT-e). A aplicação realiza consultas automatizadas em sistemas de notas fiscais, extrai dados relevantes associando-os aos motoristas cadastrados e, por fim, realiza um fechamento mensal de todas as notas transportadas por cada motorista.

🚀 Funcionalidades

✅ Automatiza a consulta de CT-es no site do IOB e, futuramente, no ÁGILIBlue.
✅ Realiza login automático e navegação com Selenium.
✅ Extrai dados como: número da nota, data de emissão, valor e status.
✅ Realiza cadastro automático de motoristas no banco de dados.
✅ Associa notas aos motoristas correspondentes.
✅ Gera registros estruturados no MySQL para posterior análise.
✅ Trata e valida dados automaticamente.
✅ Estrutura modular e extensível para futuras integrações.
✅ Exportação e gerenciamento dos dados para Excel.
✅ Modelo de licença atrelado ao tempo de uso no sistema.
✅ Envio de credenciais via SMTP.

🛠️ Tecnologias Utilizadas
Python 3.13

Selenium – Automação de navegador.

PyMySQL – Conexão com banco de dados MySQL.

MySQL – Banco de dados relacional.

Pandas – Manipulação e análise de dados.

Datetime – Manipulação de datas.

os – Interação com o sistema operacional.

PyInstaller – Empacotamento da aplicação.

PySide6 Interface gráfica.

⚙️ Pré-requisitos
Python >= 3.8 (ideal: 3.13)

MySQL >= 8.0

Navegador compatível com Selenium (Firefox recomendado)

⚠️ Observação importante:

O programa somente irá funcionar se o usuário tiver uma conta ativa e com movimentações no site do IOB.

📝 Instalação
Clone o repositório:
git clone https://github.com/LucasAnchietaAmancio/FreteLink

Crie e ative um ambiente virtual:

Para Windows: python -m venv venv e depois venv\Scripts\activate

Para Linux/macOS: python -m venv venv e depois source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

🗄️ Banco de Dados
Execute todos os scripts contidos no arquivo schemas.sql na ordem correta para criar a estrutura do banco de dados.

🤝 Contribuições
Pull Requests são bem-vindos! Para mudanças significativas, abra uma issue antes para discutir o que deseja alterar.

👤 Autor
Lucas Anchieta

📬 Contato
Email: lucasanchieta1212@gmail.com
Telefone: (66) 99646-5946
