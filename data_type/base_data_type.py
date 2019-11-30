class BaseDataType():
    def __init__(self, db, name, value=None):
        self.db = db
        self.name = name
        if value is not None:
            self.value = value

    def __str__(self):
        return str(self.value)

    def set(self, value):
        self.value = value

    def set_timeout_s(self, seconds):
        self.db.expire(self.name, seconds)

    def set_timeout_ms(self, milliseonds):
        self.db.pexpire(self.name, milliseonds)        

    def set_timeout_at_s(self, seconds):
        self.db.expireat(self.name)

    def set_timeout_at_ms(self, milliseonds):
        self.db.pexpireat(self.name)

    def unset_timeout(self):
        self.db.persist(self.name)

    def get_timeout_s(self):
        return self.db.ttl(self.name)

    def get_timeout_ms(self):
        return self.db.pttl(self.name)

    def dump(self):
        return self.db.dump(self.name)

    def load(self, value):
        return self.db.restore(self.name, ttl=0, value=value)