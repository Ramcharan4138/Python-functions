#nested function
def hi():
    def hello():
        print("inner function")
    print("outer function")
    hello()
hi()