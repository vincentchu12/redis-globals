class RedisStream():
    def __init__(self, db, name):
        self.db = db
        self.name = name

        self.db.xack(self.name,)
        self.db.xadd(self.name,)
        self.db.xclaim(self.name,)
        self.db.xdel(self.name,)
        self.db.xgroup(self.name,)
        self.db.xinfo(self.name,)
        self.db.xlen(self.name,)
        self.db.xpending(self.name,)
        self.db.xrange(self.name,)
        self.db.xread(self.name,)
        self.db.xreadgroup(self.name,)
        self.db.xrevrange(self.name,)
        self.db.xtrim(self.name,)