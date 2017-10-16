import asyncio

import logging
import uuid

from fast_orm.DBPool import DBPoolC
from TestModel import TestModelC


class DBUnitC():
    @classmethod
    def run(cls, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(DBUnitC.init(loop, **kwargs))

    @classmethod
    async def init(cls, loop, **kwargs):
        if kwargs.get('db')['is_use']:
            logging.info('DBPoolC.init start')
            dbPool = await DBPoolC.init(loop, **kwargs.get('db'))
            logging.info('DBPoolC.init end')
        rs = await TestModelC.findAll(where="name='name'", limit=(0, 5), orderBy='id')
        logging.info(rs)
        num = await TestModelC.findNumber('count(id)', where="name='name'")
        logging.info(num)
        user = await TestModelC.find('cd3dc2dab4b940a5b4dde8318a27a9d7')
        logging.info(user)
        testModel = TestModelC(id=uuid.uuid4().hex, name='name', status=2, num=123, price=111111111119,
                               content='xxxxxxx')
        result = await testModel.save()
        logging.info(result)
        testModel.name = '23277732'
        result = await testModel.update()
        logging.info(result)
        testModel1 = TestModelC(id=testModel.id)
        result = await testModel1.remove()
        logging.info(result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    db = {
        'host': 'localhost',
        'port': 3307,
        'user': 'root',
        'password': 'root',
        'db': 'fastormtest',
        'is_use': True
    }
    DBUnitC.run(
        db=db
    )
