🤖 TechNews Telegram Bot

Bot desenvolvido em Python que reúne notícias de tecnologia por meio de feeds RSS e permite consultá-las diretamente pelo Telegram. O projeto também conta com o envio automático de notícias em um horário programado.

O objetivo é facilitar o acompanhamento das novidades do mundo da tecnologia por meio de uma solução simples, automatizada e de fácil utilização.

✨ Funcionalidades

Consulta de notícias: obtenha notícias recentes de tecnologia diretamente pelo Telegram.

Integração com RSS: coleta notícias de fontes como Ars Technica e The Verge.

Envio automático: programação de envio diário de notícias às 12h30, no horário de Brasília.

Comandos interativos: utilize comandos do Telegram para iniciar o bot e solicitar notícias.

Configuração segura: o token de autenticação é carregado por meio de uma variável de ambiente.

Execução automatizada: utiliza tarefas agendadas para executar o envio de notícias.

🛠️ Tecnologias utilizadas

Python 3 — linguagem de programação.

python-telegram-bot — integração com a API do Telegram.

Feedparser — leitura e processamento de feeds RSS.

python-dotenv — carregamento de variáveis de ambiente a partir do arquivo .env.

RSS — obtenção de notícias publicadas pelas fontes configuradas.

📋 Pré-requisitos

Antes de executar o projeto, você precisará de:

Python instalado.

Uma conta no Telegram.

Um bot criado por meio do BotFather.

Um token de autenticação válido para o bot.

🚀 Instalação e configuração

1. Clone o repositório

git clone https://github.com/victoorlucass/technews-telegram-bot.git

Entre na pasta do projeto:

cd technews-telegram-bot

2. Crie um ambiente virtual

python -m venv .venv

Ative o ambiente virtual.

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

3. Instale as dependências

python -m pip install -r requirements.txt

4. Configure o token do Telegram

Na raiz do projeto, crie um arquivo chamado .env:

TELEGRAM_BOT_TOKEN=seu_token_aqui

Substitua seu_token_aqui pelo token do seu bot.

Importante: nunca compartilhe seu token nem publique o arquivo .env no GitHub.

5. Execute o bot

Com o ambiente virtual ativado, execute:

python bot.py

Após a inicialização, abra o Telegram, encontre seu bot e envie o comando /start.

💬 Comandos disponíveis

Comando

Descrição

/start

Inicia a interação com o bot.

/noticias

Solicita notícias de tecnologia.

⏰ Agendamento automático

O projeto utiliza o agendador de tarefas da biblioteca python-telegram-bot para programar o envio diário de notícias às 12h30, no horário de Brasília.

Para que o envio automático aconteça, o programa precisa permanecer em execução e ter acesso à internet.

📁 Estrutura do projeto

technews-telegram-bot/
├── .gitignore
├── bot.py
├── requirements.txt
└── README.md

bot.py: código principal do bot, incluindo a integração com o Telegram, a coleta de notícias e o agendamento.

requirements.txt: dependências necessárias para executar o projeto.

.gitignore: arquivos e pastas que não devem ser versionados.

README.md: documentação do projeto.

O arquivo .env e o ambiente virtual .venv são criados localmente e não devem ser enviados ao repositório.

🔒 Segurança

O projeto utiliza variáveis de ambiente para manter o token do Telegram separado do código-fonte.

Boas práticas adotadas:

Não versionar o arquivo .env.

Não publicar credenciais ou tokens.

Utilizar um arquivo .gitignore.

Gerenciar as dependências por meio do requirements.txt.

🎯 Objetivos de aprendizado

Este projeto foi desenvolvido com foco na prática de conceitos importantes para o desenvolvimento de software, incluindo:

Consumo e processamento de feeds RSS.

Integração com APIs e serviços externos.

Desenvolvimento de bots para o Telegram.

Gerenciamento de dependências em Python.

Utilização de variáveis de ambiente.

Automação de tarefas com agendamento.

Versionamento de código com Git e GitHub.

🔮 Possíveis melhorias futuras

Adicionar novas fontes de notícias.

Implementar filtros por categorias de tecnologia.

Permitir que o usuário personalize o horário de recebimento.

Evitar o envio de notícias duplicadas.

Criar testes automatizados.

Disponibilizar o bot em um servidor para execução contínua.

Juntar todas as notícias e pedir para alguma IA fazer uma transcrição em áudio estilo Podcast para escutar as noticias ao invés de ler.
