import asyncio

import logging

from aiohttp import web

from fast_http.AuthFactory import auth_factory
from fast_http.Jinja2Filter import datetime_filter
from fast_http.Jinja2Setting import Jinja2SettingC
from fast_http.LoggerFactory import logger_factory
from fast_http.ResponseFactory import response_factory
from fast_http.Route import RouteC


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

        app = web.Application(loop=loop, middlewares=[logger_factory, auth_factory, response_factory])
        RouteC.init(app, kwargs.get('http')['handler'], kwargs.get('http')['handler_pack'])
        if kwargs.get('http')['static'] is not None:
            RouteC.initStatic(app, kwargs.get('http')['static'])
        if kwargs.get('http')['templates'] is not None:
            Jinja2SettingC.init(app, filters=dict(datetime=datetime_filter), path=kwargs.get('http')['templates'])
        srv = await loop.create_server(app.make_handler(), kwargs.get('http')['host'], kwargs.get('http')['port'])
        logging.info(srv)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    http = {
        'host': '0.0.0.0',
        'port': 8080,
        'templates': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\templates',
        'static': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\static',
        'handler': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\handler',
        'handler_pack': 'handler.'
    }
    log = {
        'path': None,
        'name': 'py.log'
    }
    AioInitC.run(
        http=http,
        log=log
    )
