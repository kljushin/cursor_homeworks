# 2. Print current date by using 2 threads.
# #1. Define a subclass using Thread class.
# #2. Instantiate the subclass and trigger the thread.

from threading import Thread
import datetime


class DateShow(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self) -> None:
        print(f'From thread {self.name} {datetime.datetime.today().date()}')


if __name__ == '__main__':
    thread_1 = DateShow('Thread 1')
    thread_2 = DateShow('Thread 2')

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
