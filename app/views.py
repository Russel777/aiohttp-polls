from aiohttp import web
import aiohttp_jinja2

from db import Poll


class PollsList(web.View):
    @aiohttp_jinja2.template('main.html')
    async def get(self):
        polls = await Poll.query.gino.all()
        return {'polls': polls}
