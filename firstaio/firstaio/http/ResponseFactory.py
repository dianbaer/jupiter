import logging


async def response_factory(app, handler):
    async def response(request):
        logging.info('%s response_factory response start next handler %s ' % (request['first_aio_uuid'], handler))
        r = await handler(request)
        logging.info('%s response_factory response end ' % (request['first_aio_uuid']))
        return r

    return response
