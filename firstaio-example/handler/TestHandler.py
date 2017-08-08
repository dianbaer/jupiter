import uuid

import time

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
        '__user__': {
            'name': 'firstaio'
        },
        'blogs': [
            {
                'id': uuid.uuid4().hex,
                'name': 'firstaio作品展示',
                'summary': 200,
                'created_at': 1501006589.27344
            },
            {
                'id': uuid.uuid4().hex,
                'name': 'firstaio作品展示',
                'summary': 200,
                'created_at': 1501006589.27344
            },
            {
                'id': uuid.uuid4().hex,
                'name': 'firstaio作品展示',
                'summary': 200,
                'created_at': time.time()
            }
        ]

    }


@get('/1')
async def index1(*, page='1'):
    pass


@get('/blog/{id}')
async def get_blog(id):
    pass


@get('/register')
async def register(*args, **kwargs):
    return {
        '__template__': 'register1.html'
    }


@get('/signin')
async def signin():
    pass


@post('/api/authenticate')
async def authenticate(*, email, passwd):
    pass


@get('/signout')
async def signout(request):
    pass


@get('/manage/')
async def manage():
    pass


@get('/manage/comments')
async def manage_comments(*, page='1'):
    pass


@get('/manage/blogs')
async def manage_blogs(*, page='1'):
    pass


@get('/manage/blogs/create')
async def manage_create_blog():
    pass


@get('/manage/blogs/edit')
async def manage_edit_blog(*, id):
    pass


@get('/manage/users')
async def manage_users(*, page='1'):
    pass


@get('/api/comments')
async def api_comments(*, page='1'):
    pass


@post('/api/blogs/{id}/comments')
async def api_create_comment(id, request, *, content):
    pass


@post('/api/comments/{id}/delete')
async def api_delete_comments(id, request):
    pass


@get('/api/users')
async def api_get_users(*, page='1'):
    pass


@post('/api/users')
async def api_register_user(*, email, name, passwd):
    pass


@get('/api/blogs')
async def api_blogs(*, page='1'):
    pass


@get('/api/blogs/{id}')
async def api_get_blog(*, id):
    pass


@post('/api/blogs')
async def api_create_blog(request, *, name, summary, content):
    pass


@post('/api/blogs/{id}')
async def api_update_blog(id, request, *, name, summary, content):
    pass


@post('/api/blogs/{id}/delete')
async def api_delete_blog(request, *, id):
    pass
