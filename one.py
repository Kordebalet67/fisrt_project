def func1():
    print(func1.__name__)

def func2():
    print(func2.__name__)

def func3():
    print(func3.__name__)

def main():
    print(__name__)
    func1()
    func2()
    func3()

if __name__ == '__main__':
    main()
    