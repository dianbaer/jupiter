from jupiter_config.GoodDict import GoodDictC


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
