# SeCo Project #

[README English](README.md) | [JSON Specs](http://json.org/) | [MsgPack Specs](https://msgpack.org/) | [Python Docs: Pickle](https://docs.python.org/3/library/pickle.html)

## 关于SeCo项目 ##

此库可以用来方便地`序列化并压缩/去序列化并解压缩`数据，并且可以被用在各样的环境下。

用户/程序员可以方便地将Python程序中的数据序列化并压缩，并且可以将结果以`blob`的类型存入数据库中，存入`redis`或`memcached`服务器上，或者进行跨程序信息交换。

## 选择序列器和压缩器 ##

> 目前最好的组合是`msgpack`和`zlib`，此组合运行速度快并且最终结果很省空间。但是目前作为默认的组合是`json`和`zlib`因为在大多数情况下够用了。
 
但是，众所周知的是，没有一个序列器或压缩器是完美的，请根据实际情况选择。

`json`并不能处理`bytes`或者`bytearray`类型的数据；`json`和`msgpack`两者都不能处理如`set`,`frozenset`类的数据。对Python数据类型兼容性最广的是`pickle`模块，但是要注意的是`pickle`序列化的结果通常很大，而且不兼容其他语言。

`zlib`比`bz2`要快（很多），但通常情况下压缩效率并不如`bz2`。Python 3环境下还有`lzma`模块可以用作压缩，但是该模块并不存在于Python 2环境，并且压缩效率和速度不是很理想，所以并没有包含作为本库的选项。当然用户可以很方便地根据实际情况改变序列器和压缩器。

## SeCo类API文档 ##

`SeCo`是本模块提供的唯一类，可被用作`序列化并压缩/去序列化并解压缩`操作。为了提供对Python习俗的兼容，本类提供了如： `loads`, `dumps`, `load`, `dump`等方法，并且实现了`__call__`魔术方法来让用户快速操作数据.

头: `SeCo(serialize = None, compress = None)`

提供两个可选的参数来创建一个所需要的实例。

1. `serialize = None`: 第一个参数，可选`(None, 'json', 'msgpack', 'pickle')`中任意一个。

2. `compress = None`: 第二个参数，可选`(None, 'zlib', 'bz2')`中任意一个。

```python
from seco import SeCo
import json, lzma

# 使用默认的序列器和压缩器
seco = SeCo() # `json` and `zlib`
# 使用其他的序列器和压缩器
seco = SeCo('msgpack', 'bz2')
seco = SeCo('pickle', 'zlib')

# 序列化并压缩数据
#   uses __call__ method, the second parameter is the `switch`
seco({'test': 'case'}) # `bytes` object returned
seco({'test': 'case'}, True) # `bytes` object returned, the same
seco(seco({'test': 'case'}), False) # decompress, {'test': 'case'}

# Python习俗
seco.dumps(100) # `bytes` object
seco.loads(seco.dumps(100)) # 100 returned
seco.dump([1,2,3,4,5], open('test', 'wb'))
seco.load(open('test', 'rb')) # [1,2,3,4,5]

# 获取或改变序列器和压缩器
ser = seco.serializer # access the serializer
seco.serializer = json # change to json
com = seco.compressor # access the compressor
seco.compressor = lzma # change to lzma
```
