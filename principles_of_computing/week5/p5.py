__author__ = 'hrpatel'

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
