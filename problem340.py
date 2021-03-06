def crazy(n,a=50,b=2000,c=40):
	if n > b:
		return n-c
	else:
		return crazy(a + crazy(a + crazy(a + crazy(a + n))))

def crazy_eff(n, a=50, b=2000, c=40):
	if n > b:
		return n-c
	else:
		k = 1 + (b-n)/a
		return (int)(round(n + 4*k*a - (3*k+1)*c))
		
def crazy_eff_modq(n,q,a=50,b=2000,c=40):
	return (int)(round(crazy_eff(n,a,b,c)%q))
		
def S(a,b,c):
	tally = 0
	n = 0
	while n < b+1:
		tally += crazy(n,a,b,c)
		n += 1
	return tally

def S_mod(q,a,b,c):
	tally = 0
	n = 0
	while n < b+1:
		tally += crazy_eff_modq(n,q,a,b,c)
		n += 1
		if n%100000 == 0:
			print(n)
	return tally%q
	
def S_red(q,a,b,c):
	m = b/a
	a = a%q
	b = b%q
	c = c%q
	
	S1 = (4*m*a*(a-c) + m*a*b - m*a*(a-1)/2)%q
	S2 = ((m*(m-1)/2)*3*a*(a-c))%q
	S3 = ((b - m*a + 1)*(4*(m+1)*a - (3*m+4)*c) + (b - m*a)*(b - m*a + 1)/2)%q
	
	return (S1+S2+S3)%q

def main():
	a = 21**7
	b = 7**21
	c = 12**7
	q = 10**9
	
	print(S_red(q,a,b,c))
	
def test1():
	q = 10**10
	a = 50
	b = 2000
	c = 40

	x1 = crazy(b-a+1,a,b,c)
	print(x1)
	assert x1 == 3*a - 4*c + b + 1
	assert x1 == crazy_eff(b-a+1,a,b,c)
	
	x2 = crazy(b,a,b,c)
	print(x2)
	assert x2 == (4*a - 4*c + b)
	assert x2 == crazy_eff(b,a,b,c)
	
	assert crazy(0,a,b,c) == crazy_eff(0,a,b,c)

	x3 = S(a,b,c)
	assert x3%q == S_mod(q,a,b,c) and x3%q == S_red(q,a,b,c)
	print(x3)
	print(x3%q)
	
	print(S_red(q,30**10, 200**30, 12**7))
	print(S_red(q,3,2,1))
	
	print(crazy(0))
	assert crazy(0) == crazy_eff(0)
	print(crazy(2000))
	
if __name__ == "__main__":
	#test1()
	main()
