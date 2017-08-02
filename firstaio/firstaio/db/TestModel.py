import time
import uuid

from firstaio.db.Field import StringFieldC, BooleanFieldC, FloatFieldC, TextFieldC, IntegerFieldC
from firstaio.db.Model import ModelC


class TestModelC(ModelC):
    __table__ = 'users'

    id = StringFieldC(primary_key=True, default=uuid.uuid4().hex, ddl='varchar(50)')
    email = StringFieldC(ddl='varchar(50)')
    passwd = StringFieldC(ddl='varchar(50)')
    admin = BooleanFieldC()
    name = StringFieldC(ddl='varchar(50)')
    image = StringFieldC(ddl='varchar(500)')
    created_at = FloatFieldC(default=time.time)
