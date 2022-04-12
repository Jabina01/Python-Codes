def func1():
    def func2():
        print("Hello")
    return func2


def func3():
    return func1()()

func3()