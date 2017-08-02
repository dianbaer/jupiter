async def auth_factory(app, handler):
    async def auth(request):
        r = await handler(request)
        return r

    return auth
