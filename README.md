# jupiter

[![Build Status](https://travis-ci.org/dianbaer/jupiter.svg?branch=master)](https://travis-ci.org/dianbaer/jupiter)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8c69b645d91f4407a74dcf1e56d67e52)](https://www.codacy.com/app/232365732/jupiter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dianbaer/jupiter&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)


## jupiter是一个aio web框架，基于aiohttp。支持（restful格式、扫描注解、依赖注入、jinja2模板引擎、ORM框架）等。

## 核心组件介绍

--------------

### 1、jupiter_http（aio web框架）

**介绍**：基于aiohttp，扩展了``扫描注解``、``依赖注入``、``jinja2模板引擎``，支持各种请求方式。采取异步事件驱动充分发挥CPU性能。

**安装**：
```
pip install jupiter_http
```
**使用场景**：开发web项目，并且不想使用django、flask这些基于Python多线程的web框架时可以使用。

[>>>>>>性能比较网址](http://klen.github.io/py-frameworks-bench/)
	
**示例代码**：

1、返回html（get请求）
```python
@get('/')
async def index():
    return '<h1>hello world</h1>'
```
2、返回jinja2模板，模板是blogs1.html并携带__user__与blogs参数注入模板（get请求）
```python
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
            }
        ]
    }
```
3、跳转，携带关键字``redirect:``可以进行跳转（get请求）
```python
@get('/redirect')
async def redirect():
    return 'redirect:http://www.baidu.com'
```
4、POST请求，携带文件是表单请求，不携带文件是json请求（都支持，关键字``file``是表单中提取的文件）
```
@post('/api/examples')
async def api_register_user(request, *, userEmail, userName, userPassword, file=None):
    logging.info('userEmail:%s,userName:%s,userPassword:%s,file:%s' 
	% (userEmail, userName, userPassword, file))
    return {'result': 'success'}
```

5、jupiter_http框架的Demo（配置AioInit.py文件，然后启动此文件即可）

[>>>>>>jupiter_http框架的Demo](./jupiter_http_test)

----------------




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



## github：


https://github.com/dianbaer/jupiter


## 码云：

https://gitee.com/dianbaer/firstaio
	
