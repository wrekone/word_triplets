arr = [2, 4, 6, 8, 10]

def adding(n):
	return n + 1

def exponential(n):
	return n ** n

a = map(adding, arr)
x = map(exponential, arr)
b = tuple(x)
q = map(exponential, map(adding, arr))

print(list(a))
print(2+1, 4+1, 6+1, 8+1, 10+1)
print(b)
print(2**2, 4**4, 6**6, 8**8, 10**10)
print(list(q))
print((2+1)**(2+1), (4+1)**(4+1), (6+1)**(6+1), (8+1)**(8+1), (10+1)**(10+1))
