import logging
import uuid


async def logger_factory(app, handler):
    async def logger(request):
        request['first_aio_uuid'] = uuid.uuid4().hex
        logging.info('%s logger_factory logger start next handler %s ' % (request['first_aio_uuid'], handler))
        r = await handler(request)
        logging.info('%s logger_factory logger end ' % (request['first_aio_uuid']))
        return r

    return logger
