# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.

from threading import Thread
import time
import random


def some_func(delay):
    time.sleep(delay)


if __name__ == '__main__':
    threads = [Thread(target=some_func, daemon=True, args=(random.randint(5, 10),))for _ in range(10)]
    for thread in threads:
        thread.start()

    while any([t.is_alive() for t in threads]):
        print(f'{[t.is_alive() for t in threads].count(True)} threads is alive')
        time.sleep(1)
    print('All threads complete')
