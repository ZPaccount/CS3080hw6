"""
Homework 6-1
Name: Zachary Pace
Date: 3/30/2023
Description: Slow Decorator
"""
# imports
import time


# slowDown Decorator delay is 1 by default
def slowDown(func, delay=1):
    def wrapper():
        time.sleep(delay)
        func()
    return wrapper


# test function, can be anything
def test():
    print("Hello World")


# Main
slowedTest = slowDown(test, 2)
slowedTest()
