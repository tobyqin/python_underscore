# -*- coding: utf-8 -*-


# In module level

a = 'without underscore'
_a = 'single underscore prefix'  # import ignore, private member
_ = "just single score"  # one time used, import ignore


def f():
    return 'function: without underscore'


def _f():  # private member, import ignore
    return 'function: single underscore prefix'


# not recommend

a_ = 'single underscore suffix'
a__ = 'double underscore suffix'

_a_ = 'single underscore surround'
_a__ = 'single prefix + double suffix'

__a = 'double underscore prefix'
__a__ = 'double underscore surround'
__a_ = 'double prefix + single suffix'

___a = 'multiple underscore prefix'
___a___ = 'multiple underscore surround'

__ = 'just double underscore'


def _f_():
    return 'function: single underscore surround'


def __f():
    return 'function: double underscore prefix'


def __f__():
    return 'function: double underscore surround'


# In class level

class MyClass(object):
    # as class attribute
    a = 'without underscore'
    _a = 'single underscore prefix'
    __a = 'double underscore prefix'  # super private
    __a__ = 'double underscore surround'

    def f(self):
        return 'instance method: without underscore ({})'.format(self)

    def _f(self):
        return 'instance method: single underscore prefix ({})'.format(self)

    def __f(self):
        return 'instance method: double underscore prefix ({})'.format(self)

    def __f__(self):
        return 'instance method: double underscore surround ({})'.format(self)

    @staticmethod
    def s():
        return "static method: without underscore"

    # not recommend
    a_ = 'single underscore suffix'
    a__ = 'double underscore suffix'
    _a_ = 'single underscore surround'
    _a__ = 'single prefix + double suffix'
    __a_ = 'double prefix + single suffix'
    ___a = 'multiple underscore prefix'
    ___a___ = 'multiple underscore surround'

    _ = "just single score"
    __ = 'just double underscore'

    # as class instance method

    def _f_(self):  # not recommend
        return 'instance method: single underscore surround ({})'.format(self)

    # as class static method

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
