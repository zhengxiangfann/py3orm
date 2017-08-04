#-*- utf-8 -*-

class SomeClass(object):
    r"""
    Test monkey patch
    """

    def __new__(cls, *args, **kwargs):
        # super(SomeClass,cls).__new__(cls,*args,**kwargs)
        super().__new__()
        pass
    def __init__(self):
        pass
        super().__init__()

    def __str__(self):
        return SomeClass.__doc__

    def __call__(self, *args, **kwargs):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __getattr__(self, item):
        pass

    def __getattribute__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def __delete__(self, instance):
        pass


# class UpperAttrMetaClass(type):
#
#     def __new__(cls, clsname,bases,dct):
#         uppercase_attr = {}
#         for name, val in dct.items():
#             print(name+'------'+val)
#             if not name.startswith('__'):
#                 uppercase_attr[name.upper()] = val
#             else:
#                 uppercase_attr[name] = val
#         return super(UpperAttrMetaClass,cls).__new__(cls,clsname,bases,uppercase_attr)


class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)


def upper_attr(future_class_name, future_class_parents, future_class_attr):
  """
    返回一个将属性列表变为大写字母的类对象
  """

  # 选取所有不以'__'开头的属性,并把它们编程大写
  uppercase_attr = {}
  for name, val in future_class_attr.items():
      if not name.startswith('__'):
          uppercase_attr[name.upper()] = val
      else:
          uppercase_attr[name] = val

  # 用'type'创建类
  return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # 将会影响整个模块

class Foo(): # global __metaclass__ won't work with "object" though
  # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
  bar = 'bip'

print(hasattr(Foo, 'bar'))
# 输出: False
print(hasattr(Foo, 'BAR'))
# 输出: True


