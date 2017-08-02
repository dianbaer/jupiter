import asyncio

import logging
import uuid

from aiohttp import web

from firstaio.db.DBPool import DBPoolC
from firstaio.db.TestModel import TestModelC
from firstaio.http.AuthFactory import auth_factory
from firstaio.http.ResponseFactory import response_factory
from firstaio.http.Route import RouteC


class AioInitC():
    @classmethod
    def run(cls, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(AioInitC.init(loop, **kwargs))
        loop.run_forever()

    @classmethod
    async def init(cls, loop, **kwargs):
        logging.info('DBPoolC.init start')
        dbPool = await DBPoolC.init(loop, **kwargs)
        logging.info('DBPoolC.init end')
        app = web.Application(loop=loop, middlewares=[
            auth_factory, response_factory
        ])
        RouteC.init(app, 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio\\firstaio\\http\\handler',
                    'firstaio.http.handler.')
        # rs = await TestModelC.findAll(where="name='444'", limit=(5, 5), orderBy='id')
        # logging.info(rs)
        # num = await TestModelC.findNumber('count(id)', where="name='444'")
        # logging.info(num)
        # user = await TestModelC.find('00150109401573287e93a4a539c4c208819a312d01fa9d6000')
        # logging.info(user)
        # testModel = TestModelC(id=uuid.uuid4().hex, email=uuid.uuid4().hex, passwd='111', admin=True, name='2222',
        #                        image='3333')
        # result = await testModel.save()
        # logging.info(result)
        # testModel.email = '23277732'
        # result = await testModel.update()
        # logging.info(result)
        # testModel1 = TestModelC(id=testModel.id)
        # result = await testModel1.remove()
        # logging.info(result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    AioInitC.run(
        host='localhost',
        port=3307,
        user='root',
        db='awesome',
        password='root'
    )
