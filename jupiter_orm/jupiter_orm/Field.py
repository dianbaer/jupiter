class FieldC():
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringFieldC(FieldC):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchat(255)'):
        super().__init__(name, ddl, primary_key, default)


class TinyIntFieldC(FieldC):
    def __init__(self, name=None, default=0):
        super().__init__(name, 'tinyint', False, default)


class IntFieldC(FieldC):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'int', primary_key, default)


class BigIntFieldC(FieldC):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class DoubleFieldC(FieldC):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'double', primary_key, default)


class TextFieldC(FieldC):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)
