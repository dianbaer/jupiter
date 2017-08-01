from firstaio.config.ConfigDefault import firstAioConfigDefault
from firstaio.config.ConfigOverride import firstAioConfigOverride
from firstaio.config.GoodDict import GoodDict


class ConfigUtil():
    @classmethod
    def init(cls, configDefault, configOverride):
        mergeConfig = ConfigUtil.merge(configDefault, configOverride)
        global firstAioConfig
        firstAioConfig = GoodDict.toGoodDict(mergeConfig)

    @classmethod
    def merge(cls, default, override):
        r = {}
        for k, v in default.items():
            if k in override:
                if isinstance(v, dict):
                    r[k] = ConfigUtil.merge(v, override[k])
                else:
                    r[k] = override[k]
            else:
                r[k] = v
        return r


if __name__ == '__main__':
    ConfigUtil.init(firstAioConfigDefault, firstAioConfigOverride)
    print(firstAioConfig.debug)
    print(firstAioConfig.db.host)
    firstAioConfig.db.host = '172.27.108.76'
    print(firstAioConfig.db.host)
    print(firstAioConfig.db1.host1)
