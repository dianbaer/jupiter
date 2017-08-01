import logging


class ModelMetaclassC(type):
    def __new__(cls, name, bases, attrs):
        if name == 'ModelC':
            return type.__new__(cls, name, bases, attrs)
        tableName = attrs.get('__table__', None) or name
        print(tableName)
