from firstaio.config.ConfigDefault import firstAioConfigDefault
from firstaio.config.ConfigOverride import firstAioConfigOverride
from firstaio.config.ConfigUtil import ConfigUtilC

firstAioConfig = ConfigUtilC.init(firstAioConfigDefault, firstAioConfigOverride)
print(firstAioConfig.debug)
print(firstAioConfig.db.host)
firstAioConfig.db.host = '172.27.108.76'
print(firstAioConfig.db.host)
