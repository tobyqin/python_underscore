# In module level

a = 'without underscore'
a_ = 'single underscore suffix'
a__ = 'double underscore suffix'

_a = 'single underscore prefix'
_a_ = 'single underscore surround'
_a__ = 'single prefix + double suffix'

__a = 'double underscore prefix'
__a__ = 'double underscore surround'
__a_ = 'double prefix + single suffix'

___a = 'multiple underscore prefix'
___a___ = 'multiple underscore surround'

_ = "just single score"
__ = 'just double underscore'


def f():
    return 'function: without underscore'


def _f():
    return 'function: single underscore prefix'


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
    a_ = 'single underscore suffix'
    a__ = 'double underscore suffix'

    _a = 'single underscore prefix'
    _a_ = 'single underscore surround'
    _a__ = 'single prefix + double suffix'

    __a = 'double underscore prefix'
    __a__ = 'double underscore surround'
    __a_ = 'double prefix + single suffix'

    ___a = 'multiple underscore prefix'
    ___a___ = 'multiple underscore surround'

    _ = "just single score"
    __ = 'just double underscore'

    # as class instance method
    def f(self):
        return 'instance method: without underscore ({})'.format(self)

    def _f(self):
        return 'instance method: single underscore prefix ({})'.format(self)

    def _f_(self):
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
    def _s_():
        return 'static method: single underscore surround'

    @staticmethod
    def __s():
        return 'static method: double underscore prefix'

    @staticmethod
    def __s__():
        return 'static method: double underscore surround'
