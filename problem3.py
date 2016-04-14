#This at least works, just not v efficiently...
#Returns largest prime factor for a number
"""
def prime_factor(num):
	largest = 1
	for x in range(1,(num/2)+1):
		if (float(num)/x).is_integer():
			if prime_factor(x) == x:
				largest = x
	if largest == 1:
		return num
	return largest

#print prime_factor(13195)
"""

def generate_primes(num,array_of_primes):
	element = array_of_primes[len(array_of_primes)-1]
	while element != num:
		element += 1
		flag = True
		for factor in array_of_primes:
			if (float(element)/factor).is_integer() == True and factor != 1:
				flag = False
				break
		if flag == True:
			array_of_primes.append(element)
			generate_primes(num,array_of_primes)
	return array_of_primes

list_of_primes = generate_primes(7000,generate_primes(5000,generate_primes(1000,[1])))
print list_of_primes

number = 600851475143

def largest_prime_factor(number):
	largest_prime = 1
	#decomposition = []
	for prime in list_of_primes[1:]:
		remainder = float(number)/prime
		if remainder.is_integer() == True:
			largest_prime = prime
			#decomposition.append(prime)
			#print "prime", prime
			#print "remainder", remainder
			remainder_result = largest_prime_factor(remainder)
			if remainder_result > largest_prime:
				largest_prime = remainder_result
			#print "current largest prime", largest_prime
	#print decomposition
	return largest_prime

end_result = largest_prime_factor(number)
print "end_result", end_result

