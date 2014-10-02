def sum_digits(n):
	s=0
	while n:
		s += n % 10
		n /= 10
	return s
	
def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)
	
def sum_factorial_digits(n):
	return sum_digits(factorial(n))
	
def main():
	print(sum_factorial_digits(10))
	print(sum_factorial_digits(100))
	print(sum_factorial_digits(500))
	
if __name__ == "__main__":
	#test()
	main()
		 
