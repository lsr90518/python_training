def msg(func):
    from functools import wraps
    @wraps(func)
    def inner(*args, **karg):
        print("decorator message")
        func(*args, **karg)
    return inner

@msg
def test(s):
    print "test message: ",s

test("hello")



def deco(msg):
    print "decorator message: ",msg
    def inner(func):
        def ininner(s):
            func(s)
        return ininner
    return inner


@deco("Ready")
def test2(s):
    print "test2 message:", s


test2("hello")




