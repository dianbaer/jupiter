# fast_config



## 快速开始：

	pip install fast_config


	firstAioConfigOverride = {
		'db': {
			'host': '127.0.0.1',
			'port': 3307,
			'user': 'root',
			'password': 'root',
			'db': 'fastormtest',
			'is_use': True
		},
		'http': {
			'host': '0.0.0.0',
			'port': 8080,
			'templates': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\templates',
			'static': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\static',
			'handler': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\handler',
			'handler_pack': 'handler.'
		},
		'log': {
			'path': None,
			'name': 'py.log'
		}
	}
	
	firstAioConfigDefault = {
		'db': {
			'host': 'localhost',
			'port': 3306,
			'user': 'root',
			'password': 'root',
			'db': 'fastormtest',
			'is_use': True
		},
		'http': {
			'host': '0.0.0.0',
			'port': 8080,
			'templates': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\templates',
			'static': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\static',
			'handler': 'C:\\Users\\admin\\Desktop\\github\\fast\\trunk\\fast_http_test\\handler',
			'handler_pack': 'handler.'
		},
		'log': {
			'path': None,
			'name': 'py.log'
		}
	}



	import logging

	from ConfigDefault import firstAioConfigDefault
	from ConfigOverride import firstAioConfigOverride
	from fast_config.ConfigUtil import ConfigUtilC

	logging.basicConfig(level=logging.INFO)
	firstAioConfig = ConfigUtilC.init(firstAioConfigDefault, firstAioConfigOverride)
	logging.info(firstAioConfig.db.host)
	firstAioConfig.db.host = '127.0.0.1'
	logging.info(firstAioConfig.db.host)


	
