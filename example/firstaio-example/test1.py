import logging

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
