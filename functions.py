# def adder(x,y,z):
#     return x + y + z

# print(adder(1,2,3))
# print(adder(2.5, 3, 7.2))
# print(adder("a", "b", "c"))
# print(adder("fred", 1, None))

def adder(*nums):
    total = 0
    
    for num in nums:
        total += num
        # total = total + num
    
    return total

print(adder(1, 2, 3, 4, 5, 6))