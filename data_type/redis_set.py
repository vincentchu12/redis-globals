from data_type.base_data_type import BaseDataType


class RedisSet(BaseDataType):
        # self.db.smove()
        # self.db.srandmember()
        # self.db.sscan()

    """Wrapper for Redis Sets"""
    def __len__(self):
        return self.db.scard(self.name)

    def __contains__(self, x):
        return self.db.sismember(self.name, x)

    @property
    def value(self):
        return set(self.db.smembers(self.name))

    @value.setter
    def value(self, value):
        return self.db.set(self.name, value)

    def add(self, elem):
        self.db.sadd(self.name, elem)

    def update(self, *others):
        self.db.sadd(self.name, *others)

    def difference(*others):
        return self.db.sdiff(self.name, *others)

    def difference_update(self, *others):
        self.db.sdiffstore(self.name, *others)

    def intersection(self, *others):
        return self.db.sinter()

    def intersection_update(self, *others):
        self.db.sinterstore()

    def pop(self, count=None):
        self.db.spop(self.name, count)

    def discard(self, elem):
        self.db.srem(elem)

    def remove(self, elem):
        count = self.discard(self, elem)
        if count == 0:
            raise KeyError()
    def union(self, *others):
        return self.db.sunion(self.name, *others)

    def union_update(self, *others):
        self.db.sunionstore(self.name, *others)