# Redis Globals
First stab at wrapper around redis data types to align with python behavior.


To get started, create a namespace object (Redis Database) and start creating variables.
```
>>> namespace = RedisNamespace()
>>> namespace.a = 3
>>> print(namespace.a)
3

>>> namespace.a = ["hello", "world"]
print(namespace.a)
[b'hello', b'world']

>>> namespace.a.append("!")
>>> print(namespace.a)
[b'hello', b'world', b'!']

>>> namespace.b = {
...    "key1": 1,
...    "key2": 2,
... }

>>> print(namespace.b["key1"])
b'1'

>>> print(namespace.keys())
[b'key1', b'key2']

>>> print(namespace.values())
[b'1', b'2']

>>> print(namespace.b)
{b'key1': b'1', b'key2': b'2'}

>>> print("b" in namespace)
True

>>> del namespace.b
>>> print("b" in namespace)
False


```


The supported data types are:
* int (redis string)
* float (redis string)
* str (redis str)
* list (redis list)
* dict (redis hash)
* set (redis set)

