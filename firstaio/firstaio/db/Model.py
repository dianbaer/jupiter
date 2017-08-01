from firstaio.db.ModelMetaclass import ModelMetaclassC


class ModelC(dict, metaclass=ModelMetaclassC):
    def __init__(self, **kwargs):
        super(ModelC, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'ModelC' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value
