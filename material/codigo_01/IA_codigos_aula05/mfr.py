from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
quadrados = list(map(lambda x: x ** 2, nums))
pares = list(filter(lambda x: x % 2 == 0, nums))
soma = reduce(lambda acc, x: acc + x, nums, 0)
print(quadrados)
print(pares)
print(soma)
print([x ** 2 for x in nums] == quadrados)
