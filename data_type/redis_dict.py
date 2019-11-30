from data_type.base_data_type import BaseDataType


class RedisDict(BaseDataType):
    """Wrapper for Redis Hash"""
    @property
    def value(self):
        return self.db.hgetall(self.name)

    @value.setter
    def value(self, other):
        if other is self:
            return  # do nothing
        if isinstance(other, RedisDict):
            other = other.value
        self.db.delete(self.name)
        self.update(other)

    def __len__(self):  # len(d)
        return self.db.hlen(self.name)

    def __getitem__(self, key):  # d[key]
        value = self.db.hget(self.name, key)
        if value is None:
            raise KeyError()
        return value

    def __setitem__(self, key, value):  # d[key] = value
        return self.db.hset(self.name, key, value)

    def __delitem__(key):  # del d[key]
        count = self.db.hdel(self.name, key)
        if count == 0:
            raise KeyError()

    def __contains__(self, key):  # key in d, key not in d
        return self.db.hexists(self.name, key)

    def __iter__(self):  # iter(d)
        return iter(self.keys())

    def __reversed__(self):  # reversed(d)
        return iter(sorted(self.keys(), reverse=True))

    def clear(self, *keys):
        if not keys:
            keys = self.keys()
        self.db.hdel(self.name, *keys)

    def get(self, key, default=None):
        value = self[key]
        if value is None:
            return value
        return value

    def items(self):
        raise NotImplementedError()

    def keys(self):  # d.keys()
        return self.db.hkeys(self.name)

    def pop(self, key, default=None):
        if key in self:
            value = self[key]
            del self[key]
            return value
        if default:
            return default
        raise KeyError()

    def popitem(self):
        raise NotImplementedError()

    def setdefault(self, key, default=None):  # d.setdefault(key[, default])
        self.db.hsetnx(self.name, key, value)

    def update(self, other):  # d.update()
        self.db.hmset(self.name, other)

    def values(self, *keys):  # d.values()
        if keys:
            return self.db.hmget(self.name)
        else:
            return self.db.hvals(self.name)

    def inc_key(self, key, amount=1):
        if isinstance(amount, int):
            self.db.hincrby(self.name, key, amount)
        elif isinstance(amount, float):
            self.db.hincrbyfloat(self.name, key, amount)
        else:
            raise TypeError()

    def raw_key_len(self, key):
        return self.db.hstrlen(self.name, key)