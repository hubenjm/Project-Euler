import numpy as np

def main():
	N = 1000
	x = np.linspace(1,N,N)
	z1 = 3*x
	z2 = 5*x
	z3 = 15*x
	z1[z1 >= 1000] = 0
	z2[z2 >= 1000] = 0
	z3[z3 >= 1000] = 0
	
	print(z1.sum() + z2.sum() - z3.sum())

if __name__ == "__main__":
	main()
