from mypackage.foo import foo


def test_foo():
    rv = foo()
    assert rv == 'foo', '返回值不等于foo rv={}'.format(rv)
