class MagicClass(object):
    # def __new__(cls, *args, **kwargs):
    #     print 'do something in __new__()'
    #     return 'give me five!'

    def __init__(self, *args, **kwargs):
        self.title = 'qa'
        print 'do something in __init__({},{})'.format(args, kwargs)

    def __cmp__(self, other):
        return 1

    def __getattr__(self, item):
        print 'get attribute for : {}'.format(item)
        return 'hello'

    def __getattribute__(self, item):
        print 'get attribute for existed item: {}'.format(item)
        return object.__getattribute__(self, item)

mc = MagicClass(1, 2, 3)
print mc.title

