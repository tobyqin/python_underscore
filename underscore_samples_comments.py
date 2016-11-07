# -*- coding: utf-8 -*-


# In module level

a = 'without underscore'
a_ = 'single underscore suffix'  # not recommend
a__ = 'double underscore suffix'  # not recommend

_a = 'single underscore prefix'  # import ignore, private member
_a_ = 'single underscore surround'  # not recommend
_a__ = 'single prefix + double suffix'  # not recommend

__a = 'double underscore prefix'  # not recommend
__a__ = 'double underscore surround'  # not recommend
__a_ = 'double prefix + single suffix'  # not recommend

___a = 'multiple underscore prefix'  # not recommend
___a___ = 'multiple underscore surround'  # not recommend

_ = "just single score"  # one time used, import ignore
__ = 'just double underscore'  # not recommend


def f():
    return 'function: without underscore'


def _f():    # private member, import ignore
    return 'function: single underscore prefix'


def _f_():  # not recommend
    return 'function: single underscore surround'


def __f():  # not recommend
    return 'function: double underscore prefix'


def __f__():  # not recommend
    return 'function: double underscore surround'


# In class level

class MyClass(object):
    # as class attribute
    a = 'without underscore'
    a_ = 'single underscore suffix'  # not recommend
    a__ = 'double underscore suffix'  # not recommend

    _a = 'single underscore prefix'
    _a_ = 'single underscore surround'  # not recommend
    _a__ = 'single prefix + double suffix'  # not recommend

    __a = 'double underscore prefix'
    __a__ = 'double underscore surround'
    __a_ = 'double prefix + single suffix'  # not recommend

    ___a = 'multiple underscore prefix'  # not recommend
    ___a___ = 'multiple underscore surround'  # not recommend

    _ = "just single score"
    __ = 'just double underscore'  # not recommend

    # as class instance method
    def f(self):
        return 'instance method: without underscore ({})'.format(self)

    def _f(self):
        return 'instance method: single underscore prefix ({})'.format(self)

    def _f_(self):  # not recommend
        return 'instance method: single underscore surround ({})'.format(self)

    def __f(self):
        return 'instance method: double underscore prefix ({})'.format(self)

    def __f__(self):
        return 'instance method: double underscore surround ({})'.format(self)

    # as class static method
    @staticmethod
    def s():
        return "static method: without underscore"

    @staticmethod
    def _s():
        return 'static method: single underscore prefix'

    @staticmethod
    def _s_():  # not recommend
        return 'static method: single underscore surround'

    @staticmethod
    def __s():
        return 'static method: double underscore prefix'

    @staticmethod
    def __s__():
        return 'static method: double underscore surround'
