class RedisBitfield():
    """Wrapper for Redis Bitfields"""
    @property
    def value(self):
        return self.db.get(self.name)

    @value.setter
    def value(self, value):
        return self.db.set(self.name, value)

    def __getitem__(self, key):
        self.db.getbit(self.name, key)

    def __setitem__(self, key, value):
        self.db.setbit(self.name, key, value)
        # self.db.bitpos()    

    # self.db.bitcount()
    # self.db.bitfield()
    # self.db.bitop()
    
    
    