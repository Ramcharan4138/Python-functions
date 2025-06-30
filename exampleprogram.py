def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
def sfact(n):
    if n==1:
        return 1
    return fact(n)*sfact(n-1)
num=int(input("Enter a number: "))
print("Factorial",sfact(num))
