class GoodDict(dict):
    def __init__(self, **kwargs):
        super(GoodDict, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('key:%s,is not found' % item)

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def toGoodDict(cls, d):
        goodDict = GoodDict()
        for k, v in d.items():
            goodDict[k] = GoodDict.toGoodDict(v) if isinstance(v, dict) else v
        return goodDict
