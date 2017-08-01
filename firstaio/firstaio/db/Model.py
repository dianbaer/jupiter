import uuid

import time

from firstaio.db.ModelMetaclass import ModelMetaclassC
from firstaio.db.Field import StringFieldC, BooleanFieldC, FloatFieldC, TextFieldC, IntegerFieldC


class ModelC(dict, metaclass=ModelMetaclassC):
    def __init__(self, **kwargs):
        super(ModelC, self).__init__(**kwargs)
        print(self)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'ModelC' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


class TestModelC(ModelC):
    __table__ = 'test'
    id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(50)')
    admin = BooleanFieldC()
    create_at = FloatFieldC(default=time.time)
    content = TextFieldC()
    count = IntegerFieldC()
