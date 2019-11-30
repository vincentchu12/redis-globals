from data_type.base_data_type import BaseDataType


class RedisStr(BaseDataType):
    """Wrapper for Redis Strings"""
    @property
    def value(self):
        value = self.db.get(self.name)
        if value is None:
            return value
        return self.db.get(self.name).decode()

    @value.setter
    def value(self, value):
        return self.db.set(self.name, value)



    def __len__(self):
        return self.db.strlen(self.name)

    def __iadd__(self, other):
        self.db.append(self.name, other)

    def __getitem__(self, key):
        if isinstance(key, slice):
            start = 0 if key.start is None else key.start
            stop = -1 if key.stop is None else key.stop - 1  # Convert to noninclusive
            step = key.step
        elif isinstance(key, int):
            start = stop = key
            step = None
        return self.db.getrange(self.name, start, stop).decode()[::step]

        # self.db.getset()
        # self.db.mget()
        # self.db.mset()
        # self.db.msetnx()
        # self.db.psetex()
        # self.db.setex()
        # self.db.setnx()
        # self.db.setrange()
