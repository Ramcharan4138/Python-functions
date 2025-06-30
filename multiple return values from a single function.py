#multiple return values from a single function
def operate(a,b):
    return a+b, a-b, a*b
a=int(input("Enter a:"))
b=int(input("Enter b:"))
sum,diff,prod=operate(a,b)
print("Sum:",sum)
print("Subtrct:",diff)
print("Product:",prod)