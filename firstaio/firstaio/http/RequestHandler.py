import logging


class RequestHandlerC():
    def __init__(self, app, fn):
        self._app = app
        self._fn = fn

    async def __call__(self, request):
        kw = dict()
        kw['request'] = request
        logging.info('%s RequestHandlerC call start next handler %s ' % (request.__uuid__, self._fn))
        r = await self._fn(**kw)
        logging.info('%s RequestHandlerC call end ' % (request.__uuid__))
        return r
