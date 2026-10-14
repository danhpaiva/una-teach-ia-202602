def soma_profunda(x):
    if isinstance(x, list):
        return sum(soma_profunda(i) for i in x)
    return x

print(soma_profunda([1, [2, 3], [4, [5, 6]]]))
