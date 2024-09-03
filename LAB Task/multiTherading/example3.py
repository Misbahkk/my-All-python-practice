# Therading

import threading
import time


def print_num(threadName):
    for i in range(1, 11):
        print(threadName, i)


# create two threads
t1 = threading.Thread(target=print_num, args=("thread-1",))
t2 = threading.Thread(target=print_num, args=("thread-2",))

# start the threads
t1.start()
# time.sleep(0.02)  # excute the code again uncommentig this line
t2.start()

# wait for the thread to finsh
t1.join
t2.join

print("End of program")
