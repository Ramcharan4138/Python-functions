#indirect recurssion
def one(n):
    if n>0:
        print("one",n)
        two(n-1)
def two(n):
    if n>0:
        print("two",n)
        one(n//2)
num=int(input("Enter the value of n:"))
one(num)