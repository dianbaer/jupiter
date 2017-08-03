import logging

from ConfigOverride import firstAioConfigOverride
from firstaio.aioinit.AioInit import AioInitC
from firstaio.config.ConfigDefault import firstAioConfigDefault
from firstaio.config.ConfigUtil import ConfigUtilC

logging.basicConfig(level=logging.INFO)

firstAioConfig = ConfigUtilC.init(firstAioConfigDefault, firstAioConfigOverride)
logging.info(firstAioConfig.debug)
logging.info(firstAioConfig.db.host)
logging.info(firstAioConfig.db.host)
AioInitC.run(
    db=firstAioConfig.db,
    host=firstAioConfig.http.host,
    port=firstAioConfig.http.port
)
