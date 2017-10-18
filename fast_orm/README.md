# fast_orm


# fast_orm是一个AIO ORM框架，扩展了aiomysql，能够更便捷的操作数据库。

安装：

	pip install fast_orm


## 依赖：

	aiomysql
		aiomysql pymysql
		
		aiomysql-0.0.9.tar.gz
		PyMySQL-0.7.11-py2.py3-none-any.whl
	

## 推荐环境：

>快捷部署 https://github.com/dianbaer/deployment-server

	MariaDB-10.1.22

	CentOS-7-1611
	
	Python3.6


## 快速开始：

1、创建一个数据库fastormtest

	DROP TABLE IF EXISTS `example`;
	CREATE TABLE `example` (
	  `id` varchar(64) NOT NULL,
	  `name` varchar(255) NOT NULL,
	  `create_time` double NOT NULL,
	  `status` tinyint(4) NOT NULL,
	  `num` int(11) NOT NULL,
	  `price` bigint(20) NOT NULL,
	  `content` text NOT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8;
	
	
2、创建模型类

TestModelC--------模型类

	import time
	import uuid

	from fast_orm.Field import StringFieldC, TinyIntFieldC, DoubleFieldC, TextFieldC, IntFieldC, BigIntFieldC
	from fast_orm.Model import ModelC


	class TestModelC(ModelC):
		__table__ = 'example'

		id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(64)')
		name = StringFieldC(ddl='varchar(255)')
		create_time = DoubleFieldC(default=time.time)
		status = TinyIntFieldC()
		num = IntFieldC()
		price = BigIntFieldC()
		content = TextFieldC()

3、操作数据库

DBUnitC---操作数据库

	import asyncio

	import logging
	import uuid

	from fast_orm.DBPool import DBPoolC
	from TestModel import TestModelC


	class DBUnitC():
		@classmethod
		def run(cls, **kwargs):
			loop = asyncio.get_event_loop()
			loop.run_until_complete(DBUnitC.init(loop, **kwargs))

		@classmethod
		async def init(cls, loop, **kwargs):
			if kwargs.get('db')['is_use']:
				logging.info('DBPoolC.init start')
				dbPool = await DBPoolC.init(loop, **kwargs.get('db'))
				logging.info('DBPoolC.init end')
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


	if __name__ == '__main__':
		logging.basicConfig(level=logging.INFO)
		db = {
			'host': 'localhost',
			'port': 3307,
			'user': 'root',
			'password': 'root',
			'db': 'fastormtest',
			'is_use': True
		}
		DBUnitC.run(
			db=db
		)


	
