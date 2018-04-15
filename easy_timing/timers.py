from contextlib import contextmanager
from time import time


CONTEXT_MANAGER_SHOW_TIME = True
DECORATOR_SHOW_TIME = True
DECORATOR_DIGITS = 1


@contextmanager
def timer(code_description='Code executed', ndigits=1):
    """context manager to time a block of code"""
    if CONTEXT_MANAGER_SHOW_TIME:
        print(code_description)
        start = time()
        yield
        end = time()
        print('elapsed: {} seconds\n'.format(round(end - start, ndigits)))
    else:
        yield


def show_execution_time(f):
    """decorates a function or method to print the execution time"""
    if DECORATOR_SHOW_TIME:
        def decorated(*args, **kwargs):
            with timer('{} called'.format(f.__name__), ndigits=DECORATOR_DIGITS):
                return f(*args, **kwargs)
        decorated.__name__ = f.__name__
        return decorated
    else:
        return f
