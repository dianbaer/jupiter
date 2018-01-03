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
**使用场景**：开发web项目，想采取异步事件驱动模型，不想使用django、flask这些基于Python多线程的web框架时可以使用。

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
```python
@post('/api/examples')
async def api_register_user(request, *, userEmail, userName, userPassword, file=None):
    logging.info('userEmail:%s,userName:%s,userPassword:%s,file:%s' 
	% (userEmail, userName, userPassword, file))
    return {'result': 'success'}
```

5、jupiter_http框架的Demo（配置AioInit.py文件，然后启动此文件即可）

[>>>>>>jupiter_http框架的Demo](./jupiter_http_test)

----------------








### 2、jupiter_orm（aio ORM框架）

**介绍**：基于aiomysql，扩展了ORM操作数据库方式。

**安装**：
```
pip install jupiter_orm
```
**使用场景**：操作数据库，想采取异步事件驱动模型，而非阻塞式操作数据库。

**示例代码**：

1、创建实体类，继承ModelC
```python
class TestModelC(ModelC):
    __table__ = 'example'

    id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(64)')
    name = StringFieldC(ddl='varchar(255)')
    create_time = DoubleFieldC(default=time.time)
    status = TinyIntFieldC()
    num = IntFieldC()
    price = BigIntFieldC()
    content = TextFieldC()
```
2、查询列表
```python
rs = await TestModelC.findAll(where="name='name'", limit=(0, 5), orderBy='id')
```
3、查询数量
```python
num = await TestModelC.findNumber('count(id)', where="name='name'")
```
4、根据主键查询
```python
user = await TestModelC.find('cd3dc2dab4b940a5b4dde8318a27a9d7')
```
5、插入
```python
testModel = TestModelC(id=uuid.uuid4().hex, name='name', status=2, num=123, price=111111111119,
					   content='xxxxxxx')
result = await testModel.save()
```
6、修改
```python
testModel.name = '23277732'
result = await testModel.update()
```
7、删除
```python
testModel1 = TestModelC(id=testModel.id)
result = await testModel1.remove()
```
8、jupiter_orm的Demo（创建jupiterormtest.sql数据库，修改DBUnit.py配置，然后启动此文件即可）
	
[>>>>>>jupiter_orm的Demo](./jupiter_orm_test)


------



## 更多详细介绍

[>>>>>>jupiter_http详细介绍](./jupiter_http)

[>>>>>>jupiter_orm详细介绍](./jupiter_orm)

[>>>>>>jupiter_config详细介绍](./jupiter_config)

## jupiter地址：

[>>>>>>github](https://github.com/dianbaer/jupiter)

[>>>>>>码云](https://gitee.com/dianbaer/firstaio)


	
