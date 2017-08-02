from firstaio.http.HttpDecorator import get, post


@get('/')
async def index(*args, **kwargs):
    pass


@post('/users')
async def getUsers(*args, **kwargs):
    pass
