from collections import defaultdict
from math import sqrt

def compute_type_array(max_k):
	nx = [0]*(max_k+1)
	
	for h in range(1, max_k//4):
		nt = h*4 + 4
		sumx = nt
		while sumx <= max_k:
		    nx[sumx] += 1
		    nt += 8
		    sumx += nt
            
	return nx

def compute_type(n, d, max_type = 11):
	
	max_f = int(sqrt(n)) + 1
	counter = 0
	for j in range(2, max_f, 2):
		q = n // j #q = a + b, j = a - b
		w = q - j
		
		if w > 0 and q % 2 == 0 and n % j == 0 and w % 2 == 0:
			counter += 1

		if counter >= max_type:
			break
	
	if counter < max_type and counter > 0:
		d[counter].add(n)
		#print("{} is of type {}".format(n, counter))

	return counter

def compute_sum(k, d):
	S = 0
	w = set(range(1,k+1))
	for j in range(1,11):
		S += len(d[j] & w)

	return S

def main():
	#d = defaultdict(set)
	k = 1000000
	#for t in range(2,k+2,2):
	#	compute_type(t, d)

	nx = compute_type_array(k)
	print nx

if __name__ == "__main__":
	main()


