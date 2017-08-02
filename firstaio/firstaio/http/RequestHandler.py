class RequestHandlerC(object):
    def __int__(self, app, fn):
        self._app = app
        self._func = fn

    async def __call__(self, request):
        kw = None
        r = await self._func(**kw)
        return r
