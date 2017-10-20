# jupiter_http



# jupiter_http是一个AIO Web框架，扩展了aiohttp，增加扫描注解、过滤、模板等功能。

安装：

	pip install jupiter_http
	
## 依赖：

	jinja2
		jinja2 markupsafe
		
		Jinja2-2.9.6-py2.py3-none-any.whl
		MarkupSafe-1.0.tar.gz
	aiohttp
		aiohttp async_timeout chardet multidict yarl
		
		aiohttp-2.2.5-cp36-cp36m-win_amd64.whl
		async_timeout-1.2.1-py3-none-any.whl
		yarl-0.12.0-cp36-cp36m-win_amd64.whl
		multidict-3.1.3-cp36-cp36m-win_amd64.whl
		chardet-3.0.4-py2.py3-none-any.whl
	

## 推荐环境：

>快捷部署 https://github.com/dianbaer/deployment-server

	MariaDB-10.1.22

	CentOS-7-1611
	
	Python3.6


## 快速开始：

	https://github.com/dianbaer/jupiter
	jupiter_http_test项目

AioInit.py-----------启动类

	import asyncio

	import logging

	from aiohttp import web

	from jupiter_http.AuthFactory import auth_factory
	from jupiter_http.Jinja2Filter import datetime_filter
	from jupiter_http.Jinja2Setting import Jinja2SettingC
	from jupiter_http.LoggerFactory import logger_factory
	from jupiter_http.ResponseFactory import response_factory
	from jupiter_http.Route import RouteC


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
			'templates': 'D:\\github\\jupiter\\trunk\\jupiter_http_test\\templates',
			'static': 'D:\\github\\jupiter\\trunk\\jupiter_http_test\\static',
			'handler': 'D:\\github\\jupiter\\trunk\\jupiter_http_test\\handler',
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


		
TestHandler.py----------注解类
		
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
				'name': 'fast'
			},
			'blogs': [
				{
					'id': uuid.uuid4().hex,
					'name': 'fast',
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
					'name': 'fast',
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




	
## 注册服务：
		
	执行registerervice.sh
	
	包含文件
	jupiterhttptest.service
	registerervice.sh
	startservice.sh
	
