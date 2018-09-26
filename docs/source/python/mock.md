```python
import mock


def foo():
    print("foo")
    return "foo"


def test1():
    with mock.patch("__main__.foo") as mock_foo:
        foo()
        assert mock_foo.called


def test2():
    p = mock.patch("__main__.foo")
    foo()
    p.start()
    print('mock started')
    foo()
    p.stop()
    print('mock stoped')
    foo()


if __name__ == '__main__':
    test1()
    test2()
```
