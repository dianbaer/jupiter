import asyncio

import logging

from aiohttp import web

from firstaio.db.DBPool import DBPoolC
from firstaio.http.AuthFactory import auth_factory
from firstaio.http.Jinja2Filter import datetime_filter
from firstaio.http.LoggerFactory import logger_factory
from firstaio.http.ResponseFactory import response_factory
from firstaio.http.Route import RouteC
from firstaio.http.Jinja2Setting import Jinja2SettingC


class AioInitC():
    @classmethod
    def run(cls, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(AioInitC.init(loop, **kwargs))
        loop.run_forever()

    @classmethod
    async def init(cls, loop, **kwargs):
        path = kwargs.get('log')['name']
        if kwargs.get('log')['path'] is not None:
            path = kwargs.get('log')['path'] + kwargs.get('log')['name']
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            filename=path, filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)

        if kwargs.get('db')['is_use']:
            logging.info('DBPoolC.init start')
            dbPool = await DBPoolC.init(loop, **kwargs.get('db'))
            logging.info('DBPoolC.init end')

        app = web.Application(loop=loop, middlewares=[logger_factory, auth_factory, response_factory])
        RouteC.init(app, kwargs.get('http')['handler'], kwargs.get('http')['handler_pack'])
        RouteC.initStatic(app, kwargs.get('http')['static'])
        Jinja2SettingC.init(app, filters=dict(datetime=datetime_filter), path=kwargs.get('http')['templates'])
        srv = await loop.create_server(app.make_handler(), kwargs.get('http')['host'], kwargs.get('http')['port'])
        logging.info(srv)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    db = {
        'host': 'localhost',
        'port': 3307,
        'user': 'root',
        'password': 'root',
        'db': 'firstaioexample',
        'is_use': True
    }
    http = {
        'host': '0.0.0.0',
        'port': 8080,
        'templates': 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio\\firstaio\\http\\templates',
        'static': 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio\\firstaio\\http\\static',
        'handler': 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio\\firstaio\\http\\handler',
        'handler_pack': 'firstaio.http.handler.'
    }
    log = {
        'path': None,
        'name': 'py.log'
    }
    AioInitC.run(
        db=db,
        http=http,
        log=log
    )
