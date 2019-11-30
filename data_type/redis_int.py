from data_type.base_data_type import BaseDataType


class RedisInt(BaseDataType):
    """Wrapper for Redis Ints"""
    @property
    def value(self):
        value = self.db.get(self.name)
        if value is None:
            return value
        return int(value)

    @value.setter
    def value(self, other):
        if other is self:
            return  # do nothing
        if isinstance(other, RedisInt):
            other = other.value
        self.db.set(self.name, other)

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    # def __matmul__(self, other):
    #     return self.value + other

    def __truediv__(self, other):
        return self.value / other

    def __floordiv__(self, other):
        return self.value // other

    def __mod__(self, other):
        return self.value % other

    # def __divmod__(self, other):
    #     return self.value + other

    def __pow__(self, other, modulo=None):
        return pow(self.value, other, modulo)

    def __lshift__(self, other):
        return self.value << other

    def __rshift__(self, other):
        return self.value >> other

    def __and__(self, other):
        return self.value & other

    def __xor__(self, other):
        return self.value ^ other

    def __or__(self, other):
        return self.value | other

    def __radd__(self, other):
        return other + self.value

    def __rsub__(self, other):
        return other - self.value

    def __rmul__(self, other):
        return other * self.value

    # def __rmatmul__(self, other):
    #     return other + self.value

    def __rtruediv__(self, other):
        return other / self.value

    def __rfloordiv__(self, other):
        return other // self.value

    def __rmod__(self, other):
        return other % self.value

    # def __rdivmod__(self, other):
    #     return other + self.value

    def __rpow__(self, other):
        return other ** self.value

    def __rlshift__(self, other):
        return other << self.value

    def __rrshift__(self, other):
        return other >> self.value

    def __rand__(self, other):
        return other & self.value

    def __rxor__(self, other):
        return other ^ self.value

    def __ror__(self, other):
        return other | self.value

    def __iadd__(self, value):
        self.db.incrby(self.name, value)
        return self

    def __isub__(self, value):
        self.db.decrby(self.name, value)
        return self

    def __imul__(self, other):
        self.value *= other
        return self

    # def __imatmul__(self, other):
    #     return self

    def __itruediv__(self, other):
        self.value /= other
        return self

    def __ifloordiv__(self, other):
        self.value //= other
        return self

    def __imod__(self, other):
        self.value %= other
        return self

    def __ipow__(self, other, modulo):
        self.value = pow(self.value, other, modulo)
        return self

    def __ilshift__(self, other):
        self.value <<= other
        return self

    def __irshift__(self, other):
        self.value >>= other
        return self

    def __iand__(self, other):
        self.value &= other
        return self

    def __ixor__(self, other):
        self.value ^= other
        return self

    def __ior__(self, other):
        self.value |= other
        return self

    def __neg__(self):
        return - self.value

    def __pos__(self):
        return self.value

    def __abs__(self):
        return abs(self.value)

    def __invert__(self):
        return ~ self.value

    def __complex__(self):
        return (self.value)

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    def __round__(self, ndigits=None):
        return round(self.value, ndigits)

    # def __trunc__(self):
    #     return self.value

    def __floor__(self):
        return floor(self.value)

    def __ceil__(self):
        return ceil(self.value)

    def inc(self):
        self.db.incr(self.name)

    def dec(self):
        self.db.decr(self.name)
