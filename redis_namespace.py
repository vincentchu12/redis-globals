import re
import redis

# from data_type.redis_bitfield import RedisBitfield
from data_type.redis_dict import RedisDict
from data_type.redis_float import RedisFloat
from data_type.redis_int import RedisInt
from data_type.redis_list import RedisList
from data_type.redis_set import RedisSet
from data_type.redis_str import RedisStr
# from data_type.redis_stream import RedisStream

NUMBER_REGEX = r"^(?P<int>[+-]?[1-9]\d*)$|^(?P<float>[+-]?\d*[\.e]\d*)$"
NUMBER_PATTERN = re.compile(NUMBER_REGEX)


class RedisNamespace():
    def __init__(self,
                 host=u'localhost',
                 port=6379,
                 db=0,
                 password=None,
                 socket_timeout=None,
                 socket_connect_timeout=None,
                 socket_keepalive=None,
                 socket_keepalive_options=None,
                 connection_pool=None,
                 unix_socket_path=None,
                 encoding=u'utf-8',
                 encoding_errors=u'strict',
                 charset=None,
                 errors=None,
                 decode_responses=False,
                 retry_on_timeout=False,
                 ssl=False,
                 ssl_keyfile=None,
                 ssl_certfile=None,
                 ssl_cert_reqs=u'required',
                 ssl_ca_certs=None,
                 max_connections=None,
                 single_connection_client=False,
                 health_check_interval=0):

        self.db = redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            socket_timeout=socket_timeout,
            socket_connect_timeout=socket_connect_timeout,
            socket_keepalive=socket_keepalive,
            socket_keepalive_options=socket_keepalive_options,
            connection_pool=connection_pool,
            unix_socket_path=unix_socket_path,
            encoding=encoding,
            encoding_errors=encoding_errors,
            charset=charset,
            errors=errors,
            decode_responses=decode_responses,
            retry_on_timeout=retry_on_timeout,
            ssl=ssl,
            ssl_keyfile=ssl_keyfile,
            ssl_certfile=ssl_certfile,
            ssl_cert_reqs=ssl_cert_reqs,
            ssl_ca_certs=ssl_ca_certs,
            max_connections=max_connections,
            single_connection_client=single_connection_client,
            health_check_interval=health_check_interval)

        self.host = host
        self.port = port
        self.namespace = db

    def __str__(self):
        return f"RedisNamespace(namespace={self.namespace})"

    def __getattr__(self, name):
        if name in ["host", "port", "namespace"]:
            return super(RedisNamespace, self).__getattr__(name)
        if name not in self:
            raise NameError(f"name '{name}' is not defined")

        attribute_type = self.db.type(name).decode()
        if attribute_type == "string":
            attribute = RedisStr(self.db, name)
            match = NUMBER_PATTERN.match(attribute.value)                
            if match.group("int") is not None:
                return RedisInt(self.db, name)
            if match.group("float") is not None:
                return RedisFloat(self.db, name)
            return attribute
        if attribute_type == "list":
            return RedisList(self.db, name)
        if attribute_type == "hash":
            return RedisDict(self.db, name)
        if attribute_type == "set":
            return RedisSet(self.db, name)


    def __setattr__(self, name, value):
        if name in ["db", "host", "port", "namespace"]:
            super(RedisNamespace, self).__setattr__(name, value)
        elif isinstance(value, int):
            RedisInt(self.db, name).set(value)
        elif isinstance(value, float):
            RedisFloat(self.db, name).set(value)
        elif isinstance(value, bytes):
            RedisBitfield(self.db, name).set(value)
        elif isinstance(value, str):
            RedisStr(self.db, name).set(value)
        elif isinstance(value, list):
            RedisList(self.db, name).set(value)
        elif isinstance(value, dict):
            RedisDict(self.db, name).set(value)
        elif isinstance(value, set):
            RedisSet(self.db, name).set(value)
        else:
            raise ValueError(f"Unsupported data type {name}: {type(value)}")

    def __delattr__(self, name):
        if name in self:
            self.db.delete(name)
        else:
            super(RedisNamespace, self).__delattr__(name)

    def __contains__(self, x):
        return bool(self.db.exists(x))

    #     self.db.dump(self.name)
    #     self.db.keys(self.name)
    #     self.db.migrate(self.name)
    #     self.db.move(self.name)
    #     self.db.object(self.name)
    #     self.db.randomkey(self.name)
    #     self.db.rename(self.name)
    #     self.db.renamenx(self.name)
    #     self.db.restore(self.name)
    #     self.db.scan(self.name)
    #     self.db.sort(self.name)
    #     self.db.touch(self.name)
    #     self.db.type(self.name)
    #     self.db.wait(self.name)

    def delete(self, *attributes, async=False):
        if attributes:
            if async:
                self.db.unlink(*attributes)
            else:
                self.db.delete(*attributes)
        else:
            self.db.flushdb(async)

    def echo(self, value):
        return self.db.echo(value)

    def ping(self):
        return self.db.ping()
