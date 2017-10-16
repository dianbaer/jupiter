faster-http
=============


example
-------------

https://github.com/dianbaer/faster

faster-http-test

AioInit.py

	import asyncio
	import logging
	from aiohttp import web
	from faster_http.AuthFactory import auth_factory
	from faster_http.Jinja2Filter import datetime_filter
	from faster_http.Jinja2Setting import Jinja2SettingC
	from faster_http.LoggerFactory import logger_factory
	from faster_http.ResponseFactory import response_factory
	from faster_http.Route import RouteC

	class AioInitC():
		@classmethod
		def run(cls, **kwargs):
			loop = asyncio.get_event_loop()
			loop.run_until_complete(AioInitC.init(loop, **kwargs))
			loop.run_forever()

		@classmethod
		async def init(cls, loop, **kwargs):
			path = kwargs.get('log')['name']
			if kwargs.get('log')['path'] is not None:
				path = kwargs.get('log')['path'] + kwargs.get('log')['name']
			logging.basicConfig(level=logging.INFO,
								format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
								filename=path, filemode='w')
			console = logging.StreamHandler()
			console.setLevel(logging.INFO)
			formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
			console.setFormatter(formatter)
			logging.getLogger('').addHandler(console)

			app = web.Application(loop=loop, middlewares=[logger_factory, auth_factory, response_factory])
			RouteC.init(app, kwargs.get('http')['handler'], kwargs.get('http')['handler_pack'])
			if kwargs.get('http')['static'] is not None:
				RouteC.initStatic(app, kwargs.get('http')['static'])
			if kwargs.get('http')['templates'] is not None:
				Jinja2SettingC.init(app, filters=dict(datetime=datetime_filter), path=kwargs.get('http')['templates'])
			srv = await loop.create_server(app.make_handler(), kwargs.get('http')['host'], kwargs.get('http')['port'])
			logging.info(srv)


	if __name__ == '__main__':
		logging.basicConfig(level=logging.INFO)
		http = {
			'host': '0.0.0.0',
			'port': 8080,
			'templates': 'C:\\Users\\admin\\Desktop\\github\\faster\\trunk\\faster-http-test\\templates',
			'static': 'C:\\Users\\admin\\Desktop\\github\\faster\\trunk\\faster-http-test\\static',
			'handler': 'C:\\Users\\admin\\Desktop\\github\\faster\\trunk\\faster-http-test\\handler',
			'handler_pack': 'handler.'
		}
		log = {
			'path': None,
			'name': 'py.log'
		}
		AioInitC.run(
			http=http,
			log=log
		)

TestHandler.py	
		
	import uuid
	import time
	import logging
	from faster_http.HttpDecorator import get, post

	@get('/')
	async def index():
		return '<h1>hello world</h1>'

	@get('/redirect')
	async def redirect():
		return 'redirect:http://www.threecss.com'

	@get('/templates')
	async def getTemplates():
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

	@get('/register')
	async def register():
		return {
			'__template__': 'register1.html'
		}

	@post('/api/examples')
	async def api_register_user(request, *, userEmail, userName, userPassword, file=None):
		logging.info('userEmail:%s,userName:%s,userPassword:%s,file:%s' % (userEmail, userName, userPassword, file))
		return {'result': 'success'}
			
		

1、hello world
http://localhost:8080/
2、redirect
http://localhost:8080/redirect
3、use template
http://localhost:8080/templates
4、注册页，发送post请求至/api/examples，可以接受参数与文件
http://localhost:8080/register
