from firstaio.db.TestModel import TestModelC
from firstaio.http.HttpDecorator import get, post


@get('/')
async def index(*args, **kwargs):
    return '<h1>hello world</h1>'


@get('/redirect')
async def redirect(*args, **kwargs):
    return 'redirect:http://www.baidu.com'


@get('/users')
async def getUsers(*args, **kwargs):
    r = await TestModelC.findAll()
    return {
        'users': r
    }
@get('/templates')
async def getTemplates(*args, **kwargs):
    return {
        '__template__': 'blogs1.html',
    }
