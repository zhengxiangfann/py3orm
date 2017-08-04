import json


class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            print(name)
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)

# class Foo(metaclass=UpperAttrMetaclass):
#     bar = "bar"
#
# f = Foo()
# print(dir(f))
# print(hasattr(f,'BAR'))


# 类装饰器

def decorator(aclass):
    class newclass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aclass(age)
        def display(self):
            self.total_display +=1
            print('total display',self.total_display)
            self.wrapped.display()
    return newclass


@decorator
class Bird:
    def __init__(self, age):
        self.age = age
    def display(self):
        print('my age is',self.age)


# eag = Bird(5)
# for i in  range(3):
#     eag.display()

def notlogin():
    return True

CODE_NOT_LOGIN = 0
CODE_SUCCESS = 1

def login_required(fn):
    def dec_func(*args, **kwargs):
        if notlogin():
            return json.dumps({'code':CODE_NOT_LOGIN})
        else:
            return fn(*args, **kwargs)


@login_required
def cgifn(t):
    return json.dumps({'code':CODE_SUCCESS})

