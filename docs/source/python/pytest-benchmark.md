# pytest-benchmark

https://github.com/ionelmc/pytest-benchmark

`pip install pytest-benchmark`

```python
# test_benchmark.py
import time
import random


def foo():
    time.sleep(random.random() * 0.1)
    return "ok"


def bar():
    time.sleep(random.random() * 0.2)
    return "ok"


def test_foo(benchmark):
    # benchmark something
    result = benchmark(foo)
    assert result == "ok"


def test_bar(benchmark):
    result = benchmark(bar)
    assert result == "ok"


```

运行测试用例`pytest test_benchmark.py`

```
---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in ms)        Min                 Max               Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_foo              1.5631 (1.0)       97.5001 (1.0)      47.7968 (1.0)      30.1402 (1.0)       58.6010 (1.0)      48.0777 (1.42)          4;0  20.9219 (1.0)          12           1
test_bar              2.5220 (1.61)     135.0934 (1.39)     88.9072 (1.86)     43.2084 (1.43)     104.2280 (1.78)     33.8179 (1.0)           2;1  11.2477 (0.54)          7           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
====================================================================================================== 2 passed in 2.66 seconds =======================================================================================================
```
