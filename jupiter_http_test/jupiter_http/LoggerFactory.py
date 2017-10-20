import logging
import uuid


async def logger_factory(app, handler):
    async def logger(request):
        request.__uuid__ = uuid.uuid4().hex
        logging.info('%s logger_factory logger start next handler %s ' % (request.__uuid__, handler))
        r = await handler(request)
        logging.info('%s logger_factory logger end ' % (request.__uuid__))
        return r

    return logger
