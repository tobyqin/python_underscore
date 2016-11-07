class MagicClass(object):
    # def __new__(cls, *args, **kwargs):
    #     print 'do something in __new__()'
    #     return 'give me five!'

    def __init__(self, *args, **kwargs):
        print 'do something in __init__({},{})'.format(args, kwargs)


mc = MagicClass(1, 2, 3)
print mc
