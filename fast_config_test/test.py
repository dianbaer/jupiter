import logging

from ConfigDefault import firstAioConfigDefault
from ConfigOverride import firstAioConfigOverride
from fast_config.ConfigUtil import ConfigUtilC

logging.basicConfig(level=logging.INFO)
firstAioConfig = ConfigUtilC.init(firstAioConfigDefault, firstAioConfigOverride)
logging.info(firstAioConfig.db.host)
firstAioConfig.db.host = '127.0.0.1'
logging.info(firstAioConfig.db.host)
