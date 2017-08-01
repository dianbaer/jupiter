import logging

from firstaio.aioinit import AioInit
from firstaio.aioinit.AioInit import AioInitC
from firstaio.config.ConfigDefault import firstAioConfigDefault
from firstaio.config.ConfigOverride import firstAioConfigOverride
from firstaio.config.ConfigUtil import ConfigUtilC
from firstaio.db.DBPool import DBPoolC

firstAioConfig = ConfigUtilC.init(firstAioConfigDefault, firstAioConfigOverride)
print(firstAioConfig.debug)
print(firstAioConfig.db.host)
print(firstAioConfig.db.host)
logging.basicConfig(level=logging.INFO)
AioInitC.run(
    host=firstAioConfig.db.host,
    port=firstAioConfig.db.port,
    user=firstAioConfig.db.user,
    db=firstAioConfig.db.db,
    password=firstAioConfig.db.password
)