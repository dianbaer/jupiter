import asyncio

import logging
import uuid

import time

from firstaio.db.DBPool import DBPoolC
from firstaio.db.TestModel import TestModelC


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
        # rs = await DBPoolC.select("select * from users", (), 3)
        # logging.info(list(rs))
        test = TestModelC(id=uuid.uuid4().hex, admin=False, create_at=time.time, content='xxxxxx', count=1)
        logging.info(test)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    AioInitC.run(
        host='localhost',
        port=3307,
        user='root',
        db='awesome',
        password='root'
    )
