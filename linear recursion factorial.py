#linear recursion factorial
#in this we have exception limit was there ([999])
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
num=int(input("Enter a number:"))
print("Factorial:",fact(num))