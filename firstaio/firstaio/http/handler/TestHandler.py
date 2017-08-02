from firstaio.http.HttpDecorator import get, post


@get('/')
async def index(**kwargs):
    pass


@post('/users')
def getUsers(*args, **kwargs):
    pass
