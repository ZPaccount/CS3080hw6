"""
Homework 6-2
Name: Zachary Pace
Date: 3/30/2023
Description: optimizing fibonacci function
    There is a huge difference when using the Cache decorator
    it cuts down on all redundant calls to the fibonacci function
"""
# imports
import functools


# cache decorator
def cache(func):
    @functools.wraps(func)
    def wrapperCache(*args, **kwargs):
        # if args is in the cache just pull from the cache
        if args in wrapperCache.Cache.keys():
            return wrapperCache.Cache[args]
        else:
        # if args isn't in the cache add it to the cache
            wrapperCache.Cache[args] = func(*args, **kwargs)
            return wrapperCache.Cache[args]
    wrapperCache.Cache = {}
    return wrapperCache


# countCalls decorator
def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        # appends count
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)
    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls


# set wrappers
@cache
@countCalls
# Fibonacci function
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


# Main
print(fibonacci(6))
