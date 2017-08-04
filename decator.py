#-*-coding:utf-8 -*-

class mylocker:


    def __init__(self):
        print('mylocker.__init__() called.')

    @staticmethod
    def acquire():
         print('mylocker.acquire() called.')


    @staticmethod
    def unlock():
        print('mylocaker.unlock() called.')

class lockerex(mylocker):

    @staticmethod
    def acquire():
        print('lockerex.acquire() called.')

    @staticmethod
    def unlock():
        print('lockerex.unlock() called')


def lockhelp(cls):
    def _deco(func):
        def __deco(*args, **kwargs):
            print('befor %s called.'%func.__name__)
            cls.acquire()
            try:
                return func(*args,**kwargs)
            finally:
                cls.unlock()
        return __deco
    return _deco

from enum import Enum

Animal = Enum('Animal','ant bee cat dog')

class Ani:
    ant = 1
    bee = 2
    cat = 3
    dog = 4

print(Ani.ant)
print(Ani.bee)
print(Ani.dog)
print(Ani.cat)

