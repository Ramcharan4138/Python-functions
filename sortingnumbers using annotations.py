def sortnum(*args):
    return sorted(args)
nums=input("Enter numbers seperated by space:")
numbers=[int(x) for x in nums.split()]
result=sortnum(*numbers)
print(f"Sorted:{result}")
x=result[::-1]
print("Descending ",x)