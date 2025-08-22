# def adder(x, y, z):
#     return x + y + z

# print(adder(1,2,3))
# print(adder(2.5, 3, 7.2))
# print(adder("a", "b", "c"))
# print(adder("fred", 1, None))

def adder(*nums): # expect items in a box
    total = 0
    for num in nums:
        total += num
        # total = total + num
    return total

print(adder(1, 2, 3))

# numbas = [3,4,8,2,9,1]

# print(adder(*numbas))