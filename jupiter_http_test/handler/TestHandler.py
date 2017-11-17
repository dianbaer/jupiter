import uuid
import time
import logging
from jupiter_http.HttpDecorator import get, post


@get('/')
async def index():
    return '<h1>hello world</h1>'


@get('/redirect')
async def redirect():
    return 'redirect:http://www.baidu.com'


@get('/templates')
async def getTemplates():
    return {
        '__template__': 'blogs1.html',
        '__user__': {
            'name': 'jupiter'
        },
        'blogs': [
            {
                'id': uuid.uuid4().hex,
                'name': 'jupiter',
                'summary': 200,
                'created_at': 1501006589.27344
            },
            {
                'id': uuid.uuid4().hex,
                'name': 'fast',
                'summary': 200,
                'created_at': 1501006589.27344
            },
            {
                'id': uuid.uuid4().hex,
                'name': 'jupiter',
                'summary': 200,
                'created_at': time.time()
            }
        ]
    }


@get('/register')
async def register():
    return {
        '__template__': 'register1.html'
    }


@post('/api/examples')
async def api_register_user(request, *, userEmail, userName, userPassword, file=None):
    logging.info('userEmail:%s,userName:%s,userPassword:%s,file:%s' % (userEmail, userName, userPassword, file))
    return {'result': 'success'}
