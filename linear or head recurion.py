'''#recursion
#function calling without any condition
#tail recursion
#head recursion
#tree recursion
#direct and indirect recursion
#nested recursion
#linear recursion'''
#linear/head
def hrec(n):
    if n==0:
        return
    print(n)
    return hrec(n-1) #head recursion=hrec
num=int(input("Ente the value:"))
hrec(num)
def hrec(n):
    if n==0:
        return
    hrec(n-1)
    print(n)
num=int(input("Ente the value:"))
print(num)