# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.
# list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
# list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
#
from multiprocessing import Pool
import os


def common_items(list_1, list_2):
    res = set()
    set_a = set(list_1)
    set_b = set(list_2)
    return list(set_a.intersection(set_b))


if __name__ == '__main__':
    PROCESSES = os.cpu_count() - 1 or 1

    list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
    list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]

    with Pool(PROCESSES) as pool:
        result = [pool.apply(common_items, args=(list_a[i], list_b[i])) for i in range(len(min(list_a, list_b)))]
        print(result)
