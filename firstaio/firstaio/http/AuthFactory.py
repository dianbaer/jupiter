import logging


async def auth_factory(app, handler):
    async def auth(request):
        logging.info('%s auth_factory auth start next handler %s ' % (request['first_aio_uuid'], handler))
        r = await handler(request)
        logging.info('%s auth_factory auth end ' % (request['first_aio_uuid']))
        return r

    return auth
