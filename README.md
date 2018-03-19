# SeCo Project #

[README中文文档](README.zh-CN.md) | [JSON Specs](http://json.org/) | [MsgPack Specs](https://msgpack.org/) | [Python Docs: Pickle](https://docs.python.org/3/library/pickle.html)

## About the SeCo Library ##

This is a library to serialize+compress and deserialize+decompress data. It is very easy to utilize, and can be used under various environments.

By using this library, the user/developer can easily serialize+compress data in Python, like `dict`, `list` etc, save the end result as `blob` to databases, save them to `redis` or `memcached` servers, or exchange them between python processes. It can save quite some space.

## Choose Serializer and Compressor ##

> The best combination is `msgpack` and `zlib` for it is fast and space conservative. The default is `json` and `zlib` because in most cases it is sufficient.
 
However, each combination has its strengths and weaknesses, choose according to your needs.

For example, `json` cannot serialize `bytes` or `bytearray` objects; both `json` and `msgpack` cannot serialize `set`, `frozenset` instances. For the broadest possible serialization support, the user can use `pickle` as the serializer as it can serialize almost all Python objects. But remember that `pickle` is not compatible with other languages, and its result bloats quite a bit, so if you are limited by space, use the other two serializers.

Another example, `zlib` is faster, or much faster, than `bz2`, but the compressed result is not as space efficient as that of `bz2`'s. There is also `lzma` compression library available to Python 3 environment, but it is somewhat not as efficient or fast and it is not available under Python 2, so it is not included. You can absolutely change the compressor to `lzma` if you want. 

## SeCo Class API References ##

`SeCo` is the only class provided in this module, its instance is responsible for serializing + compressing and de-serializing + decompressing functionality. It provides `loads`, `dumps`, `load`, `dump` methods to conform Python conventions, and it also provides `__call__` magic method for quick operations.

Signature: `SeCo(serialize = None, compress = None)`

To construct an instance, simply provide the constructor with two optional, desired parameters.

1. `serialize = None`: the first parameter, can be anything in `(None, 'json', 'msgpack', 'pickle')`.

2. `compress = None`: the second parameter, can be anything in `(None, 'zlib', 'bz2')`.

```python
from seco import SeCo
import json, lzma

# use defaults serializer and compressor
seco = SeCo() # `json` and `zlib`
# use different serializer or compressor
seco = SeCo('msgpack', 'bz2')
seco = SeCo('pickle', 'zlib')

# serialize and compress data payload
#   uses __call__ method, the second parameter is the `switch`
seco({'test': 'case'}) # `bytes` object returned
seco({'test': 'case'}, True) # `bytes` object returned, the same
seco(seco({'test': 'case'}), False) # decompress, {'test': 'case'}

# Python conventions
seco.dumps(100) # `bytes` object
seco.loads(seco.dumps(100)) # 100 returned
seco.dump([1,2,3,4,5], open('test', 'wb'))
seco.load(open('test', 'rb')) # [1,2,3,4,5]

# access and change the serializer and compressor
ser = seco.serializer # access the serializer
seco.serializer = json # change to json
com = seco.compressor # access the compressor
seco.compressor = lzma # change to lzma
```
