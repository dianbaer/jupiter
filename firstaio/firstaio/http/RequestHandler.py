class RequestHandlerC():
    def __init__(self, app, fn):
        self._app = app
        self._fn = fn

    async def __call__(self, request):
        kw = dict()
        kw['request'] = request
        r = await self._fn(**kw)
        return r
