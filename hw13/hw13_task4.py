# 4. Divide the work between 2 methods: print_cube that returns the cube of number
# and print_square that returns the square of number. These two methods should be executed by using 2 different processes.

from concurrent.futures import ProcessPoolExecutor
import os


def print_cube(n):
    print(f'n^3 = {n * n * n}')


def print_square(n):
    print(f'n^2 = {n * n}')


if __name__ == '__main__':
    PROCESSES = os.cpu_count() - 1 or 1
    numbers = [x for x in range(100000)]
    with ProcessPoolExecutor(max_workers=PROCESSES) as pool:
        for num in numbers:
            pool.submit(print_cube, num)
            pool.submit(print_square, num)

    print('END')

