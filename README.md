# easy_timing

## installation

`python -m pip install easy-timing`


## using the context manager

```
from easy_timing import timer

with timer():
    print('hi')
```

outputs:

```
Code executed
hi
elapsed: 0.0 seconds
```

You may also give the section of code a name and optionally the number of digits to show:

```
from time import sleep

with timer('time.sleep test', ndigits=3):
    sleep(2.33)
```

which will output:

```
time.sleep test
elapsed: 2.33 seconds
```

## using the decorator
A decorator `show_execution_time` may be used on a method or function as well:

```
from easy_timing import show_execution_time

@show_execution_time
def test_func():
    print('hi')

test_func()
```

outputs:

```
test_func called
hi
elapsed: 0.0 seconds
```

## disabling during production
You can leave your `timer` and `show_execution_time` statements in the code if you like and set flags to disable or configure across all code:

```
import easy_timing
easy_timing.CONTEXT_MANAGER_SHOW_TIME = False
DECORATOR_SHOW_TIME = False
DECORATOR_DIGITS = 6
```

With these settings, no timing statements would be shown and code will execute normally. If the decorator were enabled, the statements would show up to 6 digits of precision.

## Running tests
You may test all features easily with:

`python -m easy_timing.test`
