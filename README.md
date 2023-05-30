# Checksum only python native module
I tried to find a quick python native implemenation of ip checksum to achieve a
better performance. Didn't find it, so I created my own module.
Calculate IP checksum-16 (Host endianess for compatability with other pure
python implementations:
How to use
```python
from checksum import checksum
res = checksum(b'BEST DATA')
```
The module also supports partial checksums:
```python
from checksum import checksum
res = checksum(b'BEST DATA')
res = checksum(b'ANOTHER BULK OF GREAT DATA', res)
```
