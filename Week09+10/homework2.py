"""
作业二：
自定义一个 python 函数，实现 map() 函数的功能
"""
#map(function, iter)

def map(func, iterable):
    for item in iterable:
        yield func(item)


def square(x):
    return x**2
    
if __name__ == "__main__":
    t = map(square, range(1,4))
    for i in t:
        print(i,end=',')