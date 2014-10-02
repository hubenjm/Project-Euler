import math

def isprime(n):
	if n == 1 or n%2 == 0 or n%3 == 0: return False
	elif n < 9: return True
	
	m = int(math.sqrt(n)) + 1
	i = 5
	while i <= m:
		if n%i == 0 or n%(i+2) == 0:
			return False
		i = i + 6
	return True
	
def primesum(N):
	if N <= 2: return 0
	if N == 3: return 2
	if N <= 5: return 5
	x = 5
	p = 5
	
	while p < N:
		if isprime(p): x = x+p
		p += 2
	return x
	
def main():
	print(primesum(2000000))
	
if __name__ == "__main__":
	main()
