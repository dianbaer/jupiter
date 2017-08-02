from firstaio.db.DBPool import DBPoolC
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

    @classmethod
    async def findAll(cls, where=None, args=None, **kwargs):
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kwargs.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kwargs.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await DBPoolC.select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=()):
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await DBPoolC.select(' '.join(sql), args)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']
