#This returns the prime numbers between 3 and 100

primes = [1,2]
for num in range(3,101):
	for div in range(2,num):
		s = str(num/div)
		if s[-1] == '0':
			break
		if div == (num-1):
			primes.append(num)
print(primes)