#sum of digits in given recursion
def sumD(n):
    if n==0:
        return 0
    return (n%10)+sumD(n//10)
num=int(input("Enter n:"))
print(sumD(num))