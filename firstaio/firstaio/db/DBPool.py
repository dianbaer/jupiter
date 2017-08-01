import uuid

import aiomysql
import logging

import asyncio


class DBPoolC():
    @classmethod
    async def init(cls, loop, **kwargs):
        logging.info('aiomysql.create_pool start')
        global dbPool
        dbPool = await aiomysql.create_pool(
            host=kwargs.get('host', 'localhost'),
            port=kwargs.get('port', 3306),
            user=kwargs['user'],
            password=kwargs['password'],
            db=kwargs['db'],
            charset=kwargs.get('charset', 'utf8'),
            autocommit=kwargs.get('autocommit', True),
            maxsize=kwargs.get('maxsize', 10),
            minsize=kwargs.get('minsize', 1),
            loop=loop
        )
        logging.info('aiomysql.create_pool end')
        return dbPool

    @classmethod
    async def select(cls, sql, args=(), size=None):
        uid = uuid.uuid4().hex
        logging.info("uid:%s,DBPoolC.select get conn start " % (uid,))
        with (await dbPool) as conn:
            logging.info("uid:%s,DBPoolC.select get conn end %s " % (uid, conn))
            logging.info("uid:%s,DBPoolC.select get cursor start " % (uid,))
            cur = await conn.cursor()
            logging.info("uid:%s,DBPoolC.select get cursor end %s " % (uid, cur))
            sql = sql.replace('?', '%s')
            logging.info("uid:%s,DBPoolC.select execute start " % (uid,))
            await cur.execute(sql, args)
            logging.info("uid:%s,DBPoolC.select execute end " % (uid,))
            if size:
                logging.info("uid:%s,DBPoolC.select fetchmany start " % (uid,))
                rs = await cur.fetchmany(size)
                logging.info("uid:%s,DBPoolC.select fetchmany end " % (uid,))
            else:
                logging.info("uid:%s,DBPoolC.select fetchall start " % (uid,))
                rs = await cur.fetchall()
                logging.info("uid:%s,DBPoolC.select fetchall end " % (uid,))
        return rs

    @classmethod
    async def execute(cls, sql, args=(), autocommit=True):
        uid = uuid.uuid4().hex
        logging.info("uid:%s,DBPoolC.execute get conn start " % (uid,))
        with (await dbPool) as conn:
            logging.info("uid:%s,DBPoolC.execute get conn end %s " % (uid, conn))
            if not autocommit:
                logging.info("uid:%s,DBPoolC.execute conn.begin start " % (uid,))
                await conn.begin()
                logging.info("uid:%s,DBPoolC.execute conn.begin end " % (uid,))
            try:
                logging.info("uid:%s,DBPoolC.execute get cursor start " % (uid,))
                cur = await conn.cursor()
                logging.info("uid:%s,DBPoolC.execute get cursor end %s " % (uid, cur))
                sql = sql.replace('?', '%s')
                logging.info("uid:%s,DBPoolC.execute execute start " % (uid,))
                await cur.execute(sql, args)
                affected = cur.rowcount
                logging.info("uid:%s,DBPoolC.execute execute end affected count %s " % (uid, affected))
                if not autocommit:
                    logging.info("uid:%s,DBPoolC.execute conn.commit start " % (uid,))
                    await conn.commit()
                    logging.info("uid:%s,DBPoolC.execute conn.commit end " % (uid,))
            except BaseException as e:
                if not autocommit:
                    logging.info("uid:%s,DBPoolC.execute conn.rollback start " % (uid,))
                    await conn.rollback()
                    logging.info("uid:%s,DBPoolC.execute conn.rollback end " % (uid,))
                raise
        return affected


async def testDBInit(loop):
    pool = await DBPoolC.init(loop, user='root', password='root', db='awesome', port=3307, host='localhost',
                              autocommit=False)
    rs = await DBPoolC.select("select * from users", (), 1)
    logging.info(rs)
    affectRow = await DBPoolC.execute("insert into users values(?,?,?,?,?,?,?)",
                                      (uuid.uuid4().hex, uuid.uuid4().hex, '222', 1, '444', '555', 1501094015.73242),
                                      False)
    logging.info(affectRow)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testDBInit(loop))
