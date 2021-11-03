# © SL_Jana_Team [ @SL_Jana_Team ] [ Telegram ]
# Coding : SL_Jana_Team [@SL_Jana_Team]

from aiohttp import web
from .stream_routes import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
