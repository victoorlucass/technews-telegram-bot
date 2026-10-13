
import os
import logging
import re
import html
from pathlib import Path
from dotenv import load_dotenv
from datetime import time
from zoneinfo import ZoneInfo

import feedparser
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

ARQUIVO_ENV = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=ARQUIVO_ENV, override=True)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "Token do Telegram não encontrado no arquivo .env"
    )

FUSO = ZoneInfo("America/Sao_Paulo")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


FONTES = [
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://www.theverge.com/rss/index.xml",
]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def limpar_texto(texto):
    """Remove tags HTML e espaços desnecessários."""
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = html.unescape(texto)
    return re.sub(r"\s+", " ", texto).strip()


def buscar_noticias(limite=5):
    """Busca notícias nos feeds RSS configurados."""
    noticias_encontradas = []
    links_vistos = set()

    for fonte in FONTES:
        try:
            feed = feedparser.parse(fonte)

            if feed.bozo:
                logger.warning("Feed apresentou um possível erro: %s", fonte)

            for item in feed.entries:
                titulo = limpar_texto(
                    item.get("title", "Sem título")
                )
                link = item.get("link", "")

                if not link or link in links_vistos:
                    continue

                links_vistos.add(link)

                resumo_original = item.get(
                    "summary",
                    item.get("description", ""),
                )
                resumo = limpar_texto(resumo_original)

                if len(resumo) > 350:
                    resumo = resumo[:347] + "..."

                noticias_encontradas.append({
                    "titulo": titulo,
                    "resumo": resumo,
                    "link": link,
                })

                if len(noticias_encontradas) >= limite:
                    return noticias_encontradas

        except Exception:
            logger.exception("Erro ao consultar a fonte: %s", fonte)

    return noticias_encontradas


async def enviar_noticias(
    context: ContextTypes.DEFAULT_TYPE,
    chat_id: int,
):
    resultados = buscar_noticias(limite=5)

    if not resultados:
        await context.bot.send_message(
            chat_id=chat_id,
            text="Não consegui obter notícias agora. "
                 "Tente novamente mais tarde.",
        )
        return

    await context.bot.send_message(
        chat_id=chat_id,
        text=f"☕ Bom dia! TechNews Diário\n"
             f"📰 Encontrei {len(resultados)} notícias:",
    )

    for numero, item in enumerate(resultados, start=1):
        mensagem = (
            f"{numero}. {item['titulo']}\n\n"
            f"{item['resumo']}\n\n"
            f"🔗 {item['link']}"
        )

        await context.bot.send_message(
            chat_id=chat_id,
            text=mensagem[:4000],
            disable_web_page_preview=True,
        )


async def envio_diario(
    context: ContextTypes.DEFAULT_TYPE,
):
    chat_id = context.job.chat_id
    await enviar_noticias(context, chat_id)



async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    chat_id = update.effective_chat.id
    nome_job = f"noticias_{chat_id}"

    # Evita criar vários agendamentos para o mesmo chat.
    for job in context.job_queue.get_jobs_by_name(nome_job):
        job.schedule_removal()

    context.job_queue.run_daily(
        envio_diario,
        time=time(hour=12, minute=30, tzinfo=FUSO),
        chat_id=chat_id,
        name=nome_job,
    )

    await update.message.reply_text(
        "Olá! 🤖 Seu TechNews Diário está ativo!\n\n"
        "📰 Use /noticias para receber notícias agora.\n"
        "⏰ Enviarei notícias automaticamente todos os dias "
        "às 12h30, no horário de Brasília."
    )



async def noticias(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "🔎 Buscando notícias de tecnologia..."
    )

    await enviar_noticias(
        context,
        update.effective_chat.id,
    )


def main():
    print("Diagnóstico do TechNews Bot")
    print("Arquivo:", __file__)
    print("Token existe:", bool(TOKEN))
    print("Tamanho:", len(TOKEN) if TOKEN else 0)

    if not TOKEN:
        print("ERRO: O token está vazio.")
        return

    print("Token carregado. Tentando conectar ao Telegram...")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("noticias", noticias))

    logger.info("TechNews Diário iniciado!")

    app.run_polling()


if __name__ == "__main__":
    main()