from jupiter_orm.Field import FieldC


class ModelMetaclassC(type):
    def __new__(cls, name, bases, attrs):
        if name == 'ModelC':
            return type.__new__(cls, name, bases, attrs)
        tableName = attrs.get('__table__', None) or name
        print('found ModelC: %s (table: %s)' % (name, tableName))
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, FieldC):
                print('found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    if primaryKey:
                        raise Exception('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise Exception('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey
        attrs['__fields__'] = fields
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        L = []
        for n in range(len(escaped_fields) + 1):
            L.append('?')
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (
            tableName, ', '.join(escaped_fields), primaryKey, ', '.join(L))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (
            tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        print(name, ':', attrs['__select__'])
        print(name, ':', attrs['__insert__'])
        print(name, ':', attrs['__update__'])
        print(name, ':', attrs['__delete__'])
        return type.__new__(cls, name, bases, attrs)
