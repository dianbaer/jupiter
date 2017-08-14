import time
import uuid

from firstaio.db.Field import StringFieldC, TinyIntFieldC, DoubleFieldC, TextFieldC, IntFieldC, BigIntFieldC
from firstaio.db.Model import ModelC


class TestModelC(ModelC):
    __table__ = 'example'

    id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(64)')
    name = StringFieldC(ddl='varchar(255)')
    create_time = DoubleFieldC(default=time.time)
    status = TinyIntFieldC()
    num = IntFieldC()
    price = BigIntFieldC()
    content = TextFieldC()
