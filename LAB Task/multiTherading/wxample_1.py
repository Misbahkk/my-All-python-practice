import _thread
import time


def displayNum(threadName, count, delay):
    for i in range(0, count):
        print(threadName, i)
        time.sleep(delay)
    print()


print("hello")
_thread.start_new_thread(displayNum, ("Thread-1", 5, 0.5))
_thread.start_new_thread(displayNum, ("Thread-2", 10, 1))
print("byee")
