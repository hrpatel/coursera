__author__ = 'hrpatel'

COUNT = 0

def fib(num):
    global COUNT
    COUNT += 1

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def fib_count(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return fib_count(num - 1) + fib_count(num - 2) + 1


print fib(10)
print COUNT


for i in range(10):
    COUNT = 0
    fib(i)
    print i, COUNT, fib_count(i)
