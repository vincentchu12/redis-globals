from data_type.base_data_type import BaseDataType


class RedisList(BaseDataType):
    """Wrapper for Redis lists"""
    # self.db.lpushx(self.name)
    # self.db.rpushx(self.name, *other)
    # self.db.rpoplpush(self.name)
    # self.db.ltrim(self.name)
    # self.db.linsert(self.name)
    # self.db.blpop(self.name)
    # self.db.brpop(self.name)
    # self.db.brpoplpush(self.name)
    # self.db.lpop(self.name)
    # self.db.lrange(self.name)
    def __iter__(self):
        return iter(self.value)

    @property
    def value(self):
        return self.db.lrange(self.name, 0, -1)

    @value.setter
    def value(self, other):
        if other is self:
            return  # do nothing
        if isinstance(other, RedisList):
            other = other.value
        self.db.delete(self.name)
        self.extend(other)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.db.lindex(self.name, key)
        elif isinstance(key, slice):
            start = 0 if key.start is None else key.start
            stop = -1 if key.stop is None else key.stop - 1  # Convert to noninclusive
            step = key.step
            return self.db.lrange(self.name, start, end)[::step]

    def __setitem__(self, key, value):
        self.db.lset(self.name, key, value)

    def __len__(self):
        return self.db.llen(self.name)

    def remove(x):
        self.db.lrem(self.name, 0, x)

    def pop(self):
        value = self.db.rpop(self.name)
        if value is None:
            raise KeyError()
        return value

    def prepend(self, x):
        self.db.lpush(self.name, x)

    def append(self, x):
        self.db.rpush(self.name, x)

    def extend(self, x):
        self.db.rpush(self.name, *x)

    def __iadd__(self, other):
        self.extend(other)
