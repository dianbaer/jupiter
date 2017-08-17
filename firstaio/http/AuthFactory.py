import logging


async def auth_factory(app, handler):
    async def auth(request):
        logging.info('%s auth_factory auth start next handler %s ' % (request.__uuid__, handler))
        r = await handler(request)
        logging.info('%s auth_factory auth end ' % (request.__uuid__))
        return r

    return auth
