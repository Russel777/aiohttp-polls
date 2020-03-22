import aiohttp_jinja2
import jinja2
from aiohttp import web
from db import init_db
from routes import init_routes


async def app_init():
    app = web.Application()
    init_db(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    init_routes(app)
    return app

if __name__ == '__main__':
    app = app_init()
    web.run_app(app)
