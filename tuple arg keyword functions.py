'''tuple arg keyword functions 
program to find the sum of n user input values by tuple args
syntax
def udn(*args)'''
def sumnum(*args):
    return sum(args)
nums=input("Enter numbers seperated by space:")
numbers=[float(x) for x in nums.split()]
result=sumnum(*numbers)
print(f"sum:{result}")