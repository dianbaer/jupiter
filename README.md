# firstaio

FirstAIO一款非阻塞式的Web框架，使用FirstAIO开发者可以快速的开发高并发的Web项目。


FirstAIO包含：配置、非阻塞ORM、注解、日志、模板、非阻塞Http等功能。


FirstAIO依赖：

	Python3.5+
	
	aiohttp
	
	aiomysql
	
	jinja2

快速开始：

ConfigOverride.py

	firstAioExampleConfigOverride = {
		'db': {
			'host': 'localhost',
			'port': 3307,
			'user': 'root',
			'password': 'root',
			'db': 'firstaio'
		},
		'http': {
			'host': '0.0.0.0',
			'port': 8080,
			'templates': 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio-example\\templates',
			'static': 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio-example\\static',
			'handler': 'C:\\Users\\admin\\Desktop\\github\\firstaio\\trunk\\firstaio-example\\handler',
			'handler_pack': 'handler.'
		}
	}

main.py

	from ConfigOverride import firstAioExampleConfigOverride
	from firstaio.aioinit.AioInit import AioInitC
	from firstaio.config.ConfigDefault import firstAioConfigDefault
	from firstaio.config.ConfigUtil import ConfigUtilC

	logging.basicConfig(level=logging.INFO)

	firstAioConfig = ConfigUtilC.init(firstAioConfigDefault, firstAioExampleConfigOverride)
	AioInitC.run(
		db=firstAioConfig.db,
		http=firstAioConfig.http
	)


执行指令：

python main.py
