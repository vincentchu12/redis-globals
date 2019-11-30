import redis

from redis_database import RedisDatabase


class RedisGlobals():
    class RedisNamespaces():
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
            self._namespaces = {}
            self.host = host
            self.port = port
            self.password = password
            self.socket_timeout = socket_timeout
            self.socket_connect_timeout = socket_connect_timeout
            self.socket_keepalive = socket_keepalive
            self.socket_keepalive_options = socket_keepalive_options
            self.connection_pool = connection_pool
            self.unix_socket_path = unix_socket_path
            self.encoding = encoding
            self.encoding_errors = encoding_errors
            self.charset = charset
            self.errors = errors
            self.decode_responses = decode_responses
            self.retry_on_timeout = retry_on_timeout
            self.ssl = ssl
            self.ssl_keyfile = ssl_keyfile
            self.ssl_certfile = ssl_certfile
            self.ssl_cert_reqs = ssl_cert_reqs
            self.ssl_ca_certs = ssl_ca_certs
            self.max_connections = max_connections
            self.single_connection_client = single_connection_client
            self.health_check_interval = health_check_interval

        def __str__(self):
            database_repr = []
            for database in self._namespaces.values():
                database_repr.append(str(database))
            return f'RedisNamespaces[{", ".join(database_repr)}]'

        def __getitem__(self, db):
            if db not in self._namespaces:
                self._namespaces[db] = RedisDatabase(
                    host=self.host,
                    port=self.port,
                    db=db,
                    password=self.password,
                    socket_timeout=self.socket_timeout,
                    socket_connect_timeout=self.socket_connect_timeout,
                    socket_keepalive=self.socket_keepalive,
                    socket_keepalive_options=self.socket_keepalive_options,
                    connection_pool=self.connection_pool,
                    unix_socket_path=self.unix_socket_path,
                    encoding=self.encoding,
                    encoding_errors=self.encoding_errors,
                    charset=self.charset,
                    errors=self.errors,
                    decode_responses=self.decode_responses,
                    retry_on_timeout=self.retry_on_timeout,
                    ssl=self.ssl,
                    ssl_keyfile=self.ssl_keyfile,
                    ssl_certfile=self.ssl_certfile,
                    ssl_cert_reqs=self.ssl_cert_reqs,
                    ssl_ca_certs=self.ssl_ca_certs,
                    max_connections=self.max_connections,
                    single_connection_client=self.single_connection_client,
                    health_check_interval=self.health_check_interval)
            return self._namespaces[db]

        def __delitem__(self, db):
            database = self._namespaces.pop(db, None)
            if database is None:
                raise KeyError()
            database.delete()

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

        self._namespaces = RedisGlobals.RedisNamespaces(
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

    @property
    def namespaces(self):
        return self._namespaces

    @namespaces.deleter
    def namespaces(self):
        self._namespaces[0].db.flushall(False)

    def __str__(self):
        return f"RedisGlobals(host={self.host}, port={self.port})"

server = RedisGlobals()
server.namespaces[0]

# del server.namespaces[0]
# print(server.namespaces[1])
# print(server.namespaces)
# print(server)
server.namespaces[0].a = {"efpo": 89, "ifje": 38, "eofj": 3890}

server.namespaces[0].d = 58

server.namespaces[0].d

# auth
# quit
# select
# swapdb