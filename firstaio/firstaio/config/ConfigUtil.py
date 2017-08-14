import logging

from firstaio.config.ConfigDefault import firstAioConfigDefault
from firstaio.config.ConfigOverride import firstAioConfigOverride
from firstaio.config.GoodDict import GoodDictC


class ConfigUtilC():
    @classmethod
    def init(cls, configDefault, configOverride):
        mergeConfig = ConfigUtilC.merge(configDefault, configOverride)
        firstAioConfig = GoodDictC.toGoodDict(mergeConfig)
        return firstAioConfig

    @classmethod
    def merge(cls, default, override):
        r = {}
        for k, v in default.items():
            if k in override:
                if isinstance(v, dict):
                    r[k] = ConfigUtilC.merge(v, override[k])
                else:
                    r[k] = override[k]
            else:
                r[k] = v
        return r


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    firstAioConfig = ConfigUtilC.init(firstAioConfigDefault, firstAioConfigOverride)
    logging.info(firstAioConfig.db.host)
    firstAioConfig.db.host = '127.0.0.1'
    logging.info(firstAioConfig.db.host)
