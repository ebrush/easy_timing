from functools import partial
from time import sleep

from timers import timer, show_execution_time


def test_timer_context_manager():
    with timer('str joins', 3):
        full_doc = ''.join(map(str, range(1000000)))

    with timer('progressive str appending'):
        full_doc = ''
        for i in range(1000000):
             full_doc += str(i)

    with timer('list comprehensions'):
        length = len([str(i) for i in range(1000000)])

    with timer('partials'):
        length = len(list(map(partial(str), range(1000000))))

    with timer('lambdas'):
        length = len(list(map(lambda i: str(i), range(1000000))))


def test_timer_decorator():
    @show_execution_time
    def a_function_that_sleeps():
        sleep(2)

    class TestClass:
        def __init__(self, what_to_print='I\'m going to wait'):
            self.what_to_print = what_to_print

        @show_execution_time
        def a_method_that_sleeps(self):
            print(self.what_to_print)
            sleep(2)

    a_function_that_sleeps()
    TestClass().a_method_that_sleeps()


if __name__ == '__main__':
    test_timer_context_manager()
    test_timer_decorator()

    # the below will show how you can turn off the displays
    import timers
    timers.CONTEXT_MANAGER_SHOW_TIME = False
    timers.DECORATOR_SHOW_TIME = False
    test_timer_context_manager()
    test_timer_decorator()
