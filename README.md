# jupiter

[![Build Status](https://travis-ci.org/dianbaer/jupiter.svg?branch=master)](https://travis-ci.org/dianbaer/jupiter)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8c69b645d91f4407a74dcf1e56d67e52)](https://www.codacy.com/app/232365732/jupiter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dianbaer/jupiter&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)


## jupiter是一个AIO web框架,能够快速开发高性能web项目。支持扫描注解、过滤、模板、ORM等。

## 此项目问题反馈与答疑QQ群：537982451

## github：


https://github.com/dianbaer/jupiter


## 码云：

https://gitee.com/dianbaer/firstaio


### 1、jupiter_http


jupiter_http是一个AIO Web框架，扩展了aiohttp，增加扫描注解、过滤、模板等功能。

>安装：
	
	pip install jupiter_http
	
	
>代码示例：

	
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


>例子：


[jupiter_http_test](./jupiter_http_test)


[jupiter_http详细介绍](./jupiter_http)



### 2、jupiter_orm


jupiter_orm是一个AIO ORM框架，扩展了aiomysql，能够通过对象操作数据库。


>安装：

	pip install jupiter_orm
	

>代码示例：


	class TestModelC(ModelC):
		__table__ = 'example'

		id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(64)')
		name = StringFieldC(ddl='varchar(255)')
		create_time = DoubleFieldC(default=time.time)
		status = TinyIntFieldC()
		num = IntFieldC()
		price = BigIntFieldC()
		content = TextFieldC()
		

	rs = await TestModelC.findAll(where="name='name'", limit=(0, 5), orderBy='id')
	logging.info(rs)
	num = await TestModelC.findNumber('count(id)', where="name='name'")
	logging.info(num)
	user = await TestModelC.find('cd3dc2dab4b940a5b4dde8318a27a9d7')
	logging.info(user)
	testModel = TestModelC(id=uuid.uuid4().hex, name='name', status=2, num=123, price=111111111119,
						   content='xxxxxxx')
	result = await testModel.save()
	logging.info(result)
	testModel.name = '23277732'
	result = await testModel.update()
	logging.info(result)
	testModel1 = TestModelC(id=testModel.id)
	result = await testModel1.remove()
	logging.info(result)
	

>例子：


[jupiter_orm_test](./jupiter_orm_test)


[jupiter_orm详细介绍](./jupiter_orm)



### 3、jupiter_config

>安装：

	pip install jupiter_config
	
	
[jupiter_config详细介绍](./jupiter_config)




### 上传至pypi


	windows 创建文件

	type NUL > .pypirc

	.pypric文件放入home目录下

		[distutils]
		index-servers =
		  pypi

		[pypi]
		repository=https://pypi.python.org/pypi
		username=your_username
		password=your_password

	检查	
	python setup.py check

	打包
	python setup.py sdist

	上传
	python setup.py sdist upload -r pypi



	
