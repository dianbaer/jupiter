import logging


class RequestHandlerC():
    def __init__(self, app, fn):
        self._app = app
        self._fn = fn

    async def __call__(self, request):
        kw = dict()
        kw['request'] = request
        logging.info('%s RequestHandlerC call start next handler %s ' % (request['first_aio_uuid'], self._fn))
        r = await self._fn(**kw)
        logging.info('%s RequestHandlerC call end ' % (request['first_aio_uuid']))
        return r
