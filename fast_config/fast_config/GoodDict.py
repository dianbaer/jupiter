class GoodDictC(dict):
    def __init__(self, **kwargs):
        super(GoodDictC, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'GoodDictC' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def toGoodDict(cls, d):
        goodDict = GoodDictC()
        for k, v in d.items():
            goodDict[k] = GoodDictC.toGoodDict(v) if isinstance(v, dict) else v
        return goodDict
