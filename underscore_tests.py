def to_string(obj):
    if callable(obj):
        try:
            msg = obj()
        except Exception as e:
            msg = 'Error: ' + e.message
    else:
        msg = "{}".format(obj)

    if len(msg) > 60:
        return "{}...{}".format(msg[:30:], msg[-30::])
    else:
        return msg


def get_all_attributes():
    return ['a', 'a_', 'a__', '_a', '_a_', '_a__', '__a', '__a__', '__a_', '___a', '___a___', '_', '__']


def get_all_funcs():
    return ['f', '_f', "_f_", '__f', '__f__']


def get_all_static_methods():
    return ['s', '_s', "_s_", '__s', '__s__']


def get_all_defined(in_class=False):
    l = get_all_attributes()
    l.extend(get_all_funcs())

    if in_class:
        l.extend(get_all_static_methods())
        return l
    else:
        return l


def verify_underscore(obj, a_format, f_format, in_class=False):
    if hasattr(obj, 'keys'):
        names = obj.keys()
        get = lambda x: obj[x]
    else:
        names = dir(obj)
        get = lambda x: getattr(obj, x)

    defined = get_all_defined(in_class=in_class)
    attr = []
    func = []
    missing = []

    for name in defined:
        if name in names:
            if callable(get(name)):
                func.append(name)
            else:
                attr.append(name)
        else:
            missing.append(name)

    print
    print " attributes ".center(50, '=')
    for name in sorted(attr)[::-1]:
        print a_format.format(name, to_string(get(name)))

    print
    print " functions ".center(50, '=')
    for name in sorted(func)[::-1]:
        print f_format.format(name, to_string(get(name)))

    extra = set(names) - set(defined)
    extra = [x for x in extra if '_' in x]
    if len(extra):
        print
        print " extra underscores names ".center(50, '=')
        for name in sorted(extra):
            print name

    if len(missing):
        print
        print " missing underscores names ".center(50, '=')
        for name in missing:
            print name

    print
    print " end ".center(50, '=')


def test_underscore_in_module_by_import():
    import underscore_samples
    print "\nimport underscore_samples module"
    d = underscore_samples.__dict__
    verify_underscore(d, "underscore_samples.{} = {}", "underscore_samples.{}() = {}")


def test_underscore_in_module_by_from_import():
    from underscore_samples import *
    print "\nfrom underscore_samples import *"
    d = locals()
    verify_underscore(d, "{} = {}", "{}() = {}")


def test_underscore_in_class_instance():
    import underscore_samples
    print "\nVerify underscore defined in class instance"
    test_class = underscore_samples.MyClass()
    verify_underscore(test_class, "test_class.{} = {}", "test_class.{}() = {}", in_class=True)


def test_underscore_in_class_static():
    import underscore_samples
    print "\nVerify underscore defined in class type"
    verify_underscore(underscore_samples.MyClass.__dict__, "MyClass.{} = {}", "MyClass.{}() = {}", in_class=True)
