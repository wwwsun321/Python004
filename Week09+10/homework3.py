""""
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数
"""

import time
def timer(func):
    def inner(*args, **kwargs):
        starttime = time.time()
        func(*args, **kwargs)
        endtime = time.time()
        print(f"args:{args},kwargs:{kwargs},func:{func.__name__} spend time:{endtime - starttime}")
    return inner
@timer
def function1(*args, **kwargs):
    time.sleep(1)

if __name__ == "__main__":
    function1(1,{'a':1},d=5,f=6)