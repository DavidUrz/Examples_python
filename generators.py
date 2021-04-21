# Usar grandes listas o datos 1 a la vez
def gen(n):
    for i in range(n):
        yield i ** 2

g = gen(1000)
for i in g:
    print(i)