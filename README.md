# objects_clipboard!
[![Python 3.7.1](https://img.shields.io/badge/Python-3.7.1-green.svg)](http://www.python.org/download/)

A  clipboard for python objects

what objects_clipboard do for you?
----
* copy objects between two python shells, fast easy
* store objects to use later
* unlimited storing capacity (in range of your ram's)

You can either install from pypi or  the source code
1) Using pip
```bash
pip install objects_clipboard
```
2) from the source code
```bash
git clone https://github.com/n0x1s/objects_clipboard
cd cached_properties
pip install -e .
```
## How to use

Let us suppose you have two python REPL and you want to copy Response object (requests) to the another shell
1) source machine
```python
# source machine

>>> from objects_clipboard import ObjectsClipboard
>>> clipboard = ObjectsClipboard(capacity=None, obj_maxsize=None)
# storing object
>>> obj = requests.get('https://python.org')
>>> clipboard.store(obj)
>>> clipboard.store([5] * 5e6)
# copying object
>>> clipboard.copy(0) # by default copy take the last item that was saved > -1
> True
```
2) target machine
```python
# target machine
# after you copied the object from the first machine
>>> from objects_clipboard import ObjectsClipboard
>>> obj = ObjectsClipboard.paste()
>>> print(obj)
> <Response [200]>
```
## Todo
I will try to maintain this respiratory and update or add new things to it you are welcome to contribute :relaxed:

Here some of the following features:

- [ ] Support sessions storing (save objects for later use)
- [ ] Support online labs (G-colab, jupyter ...)
- [ ] Support global sharing (sharing objects between two machine)

And, as always have a beautiful day!
