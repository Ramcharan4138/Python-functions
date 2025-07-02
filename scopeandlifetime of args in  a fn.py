# scope and lifetime of args in a function
num=10
print(num)
def modify():
    global num
    num=100
modify()
print(num)