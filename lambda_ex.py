terms = 8
# def powers_of_two(terms):
#     result = []
#     for x in range(terms):
#         result.append(2 ** x)
#     return result

# print(powers_of_two(terms))

result = list(map(lambda x: 2 ** x, range(terms)))

print(result)
