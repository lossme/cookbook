## pytest 常规使用

目录结构

```sh
tests
├── __init__.py
├── test_bar.py
└── test_foo.py
```


```python
# test_foo.py
def test_foo():
    print('foo')
```


```python
# test_bar.py
def test_bar1():
    print('bar1')

def test_bar2():
    print('bar2')
```




```sh
# 运行tests文件夹下的所有测试（会自动收集以test开头的文件和test开头的方法，并进行测试）
# -s 捕获标准输出，这样才能看到 print 输出的内容， -v 输出更多的信息
>>> pytest tests/ -s -v
============================= test session starts =============================
platform linux -- Python 3.6.4, pytest-3.3.1, py-1.5.2, pluggy-0.6.0 -- /home/key/anaconda3/bin/python
cachedir: .cache
rootdir: /home/key/test, inifile:
plugins: cov-2.5.1
collected 4 items

tests/test_bar.py::test_bar1 bar1
PASSED                                     [ 25%]
tests/test_bar.py::test_bar2 bar2
PASSED                                     [ 50%]
tests/test_foo.py::test_foo1 foo1
PASSED                                     [ 75%]
tests/test_foo.py::test_foo2 foo2
PASSED                                     [100%]

========================== 4 passed in 0.01 seconds ===========================
```

```
# 只运行这个tests/test_bar.py测试文件
>>> pytest tests/test_bar.py -s -v

# 只运行 tests/test_bar.py里的test_bar方法
>>> pytest tests/test_bar.py::test_bar -s -v

# 只测匹配的
>>> pytest tests/test_bar.py -k test_bar -s -v

```
