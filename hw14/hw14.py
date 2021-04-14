import time
import glob
import concurrent.futures


def find_pattern_line(path, pattern):
    result = set()
    with open(path) as file:
        for line in file:
            if pattern in line:
                result.add(line)
    return result


def find_by_pattern_threads(path, pattern):
    files = glob.glob(f'{path}**/*.py', recursive=True)
    result = set()
    with concurrent.futures.ThreadPoolExecutor() as thread_pool:
        find_res = thread_pool.map(find_pattern_line, files, [pattern] * len(files))
        for res in find_res:
            result.update(res)
    return result


def find_by_pattern_process(path, pattern):
    files = glob.glob(f'{path}**/*.py', recursive=True)
    result = set()
    with concurrent.futures.ProcessPoolExecutor() as process_pool:
        find_res = process_pool.map(find_pattern_line, files, [pattern] * len(files))
        for res in find_res:
            result.update(res)
    return result


if __name__ == '__main__':
    print('Threads')
    start = time.time()
    print(find_by_pattern_threads('/home/klush/PycharmProjects/cursor_homeworks/', pattern='import'))
    end = time.time()
    print(f'Execution time {end-start}')

    print('Processes')
    start = time.time()
    print(find_by_pattern_threads('/home/klush/PycharmProjects/cursor_homeworks/', pattern='import'))
    end = time.time()
    print(f'Execution time {end - start}')
