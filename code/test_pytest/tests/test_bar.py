from mypackage.bar import bar


def test_bar():
    rv = bar()
    assert rv == 'bar', '返回值不等于bar rv={}'.format(rv)
