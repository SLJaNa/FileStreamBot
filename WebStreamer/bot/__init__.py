# This file is a part of SL_Jana_File to URL Uploader_Bot
# Coding : 𝙎𝙇_𝙅𝙖𝙣𝙖_𝙏𝙚𝙖𝙢 [@SL_Jana_Team]

from pyrogram import Client
from ..vars import Var

StreamBot = Client(
    session_name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
