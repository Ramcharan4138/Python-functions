#nested function
def operation(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    print("Addition:",add())
    print("Subtract:",sub())
a=int(input("Enter a:"))
b=int(input("Enter b:"))
operation(a,b)