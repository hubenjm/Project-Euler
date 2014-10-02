def gcd(a,b):
	while b:
		a, b = b, a%b
	return a
	
def lcm1toN(N):
	i = 1
	lcm = 1
	while(i <= N):
		lcm = lcm*i/gcd(lcm,i)
		i += 1
	return lcm
	
def main():
	print(lcm1toN(200))
	
if __name__ == "__main__":
	main()
