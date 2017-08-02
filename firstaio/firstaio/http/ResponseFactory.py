async def response_factory(app, handler):
    async def response(request):
        r = await handler(request)
        return r

    return response
