__author__ = 'hrpatel'

COUNT = 0

def memoized_fib(num, memo_dict):
    global COUNT
    COUNT += 1

    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

print memoized_fib(10, {0 : 0, 1 : 1})
print COUNT
print

for i in range(1, 10):
    COUNT = 0
    print i, memoized_fib(i, {0 : 0, 1 : 1}), COUNT
