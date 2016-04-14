def fibonacci_recursive(index):
	if index == 1 or index == 2:
		return index
	return fibonacci_recursive(index-1) + fibonacci_recursive(index - 2)

array = []

i = 1
while fibonacci_recursive(i) < 4000000:
	if fibonacci_recursive(i) % 2 == 0:
		array.append(fibonacci_recursive(i))
	i += 1

print sum(array)

