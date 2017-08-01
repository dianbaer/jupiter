import time
import uuid

from firstaio.db.Field import StringFieldC, BooleanFieldC, FloatFieldC, TextFieldC, IntegerFieldC
from firstaio.db.Model import ModelC


class TestModelC(ModelC):
    __table__ = 'test'
    id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(50)')
    admin = BooleanFieldC()
    create_at = FloatFieldC(default=time.time)
    content = TextFieldC()
    count = IntegerFieldC()
