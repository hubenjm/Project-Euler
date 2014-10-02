def f1(n):
	return (1-(-n)**11)/(1+n)
	
def f2(n):
	return n**3
    
def FIT(f,k):
	#k = number of points to use when fitting (e.g. 2 for a line, 3 for quadratic)
	y = [f(i) for i in range(1,k+1,1)]
	sign = (-1)**(k-1)
	binomcoeff = 1
	result = 0
	for j in range(0,k,1):
		result += sign*binomcoeff*y[j]
		sign *= -1
		binomcoeff = binomcoeff*(k-j)/(j+1)
	
	return result
	
def sumFIT(f,N):
	x = 0
	for k in range(1,N+1,1):
		x += FIT(f,k)
	return x	

def test():
	print f(3)
	print f(0)
	print f(1)
	xi = [i for i in range(1,11,1)]
	yi = [f1(i) for i in range(1,11,1)]
	print(xi)
	print(yi)
	
def main():
	print(sumFIT(f1, 10))
	print(sumFIT(f2, 3))
	
if __name__ == "__main__":
	#test()
	main()
