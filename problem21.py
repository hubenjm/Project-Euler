def proper_factors(n):
	a, r = 1, [1]
	while a * a < n:
		a += 1
		if n % a: continue
		b, f = 1, []
		while n % a == 0:
			n //= a
			b *= a
			f += [i * b for i in r]
		r += f
	if n > 1: r += [i * n for i in r]
	return r[:-1]
	
def find_amicable(N):
	r = []
	a=1
	while a < N:
		if not a in r:
			b = sum(proper_factors(a))
			if b != a and sum(proper_factors(b)) == a:
				r += [a,b]
		a += 1
	return r
	
def test():
	print(proper_factors(220))
	print(proper_factors(28))
	print(sum(proper_factors(220)))
	
	print(find_amicable(30))
	
def main():
	print(sum(find_amicable(10000)))
		
if __name__ == "__main__":
	test()
	main()
		
