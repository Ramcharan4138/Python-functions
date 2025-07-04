'''write a code to check the given number is even or odd using in-direct recursive method with boolean output
input=5
output=5 is even" False'''
def is_even(n):     #n=5   n=3                               n=1   
    if n == 0:      #n==5  n==3                              n==1
        return True

    return is_odd(n - 1)     #is_odd(4)    is_odd(2)         i_od(0)   
def is_odd(n):               #n=4            n=2              n=0
    if n == 0:               #n==4           n==2             false
        return False        
    return is_even(n - 1)    #is_even(3)      is_even(1)
num = int(input("Enter a number:"))
print(num, "is odd?",is_even(num))
