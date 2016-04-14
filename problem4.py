def check_palindrome(number):
	number_string = str(number)
	half_length = len(number_string)/2
	for x in range(0,half_length):
		if number_string[x] == number_string[len(number_string)-1-x]:
			continue
		else:
			return False
	return True

def main_function(num1):
	for y in range(999,99,-1):
		product = num1 * y
		if check_palindrome(product) == True:
			array_of_palindromes.append(product)
			return
	return

array_of_palindromes = []

for x in range(999,99,-1):
	main_function(x)

print max(array_of_palindromes)