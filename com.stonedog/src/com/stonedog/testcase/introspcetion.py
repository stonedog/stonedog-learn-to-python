def test_inspect_stack():
    import inspect
    stacks=inspect.stack()
    for s in stacks:
        print s

test_inspect_stack()

def print_callers(func):
    import inspect
    def f(*args, **kwargs):
        stacks = inspect.stack()
        index = 1
        stack = stacks[index]
        while stack[1] == "<string>":
            index = index + 1
            stack = stacks[index]
        print stack[1], "line", stack[2]
        print "".join(stack[4])
        return func(*args, **kwargs)
    return f

@print_callers
def f(a,b):
    return a+b
    
f(1,2)
tmp = f
tmp(4,5)
eval("f(5,6)")