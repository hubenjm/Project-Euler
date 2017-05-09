import numpy as np

def find_largest_reciprocal_period(d_max):
	assert d_max > 1

	max_length = 0
	d_best = 1

	for d in xrange(1,d_max + 1):

		#find first non-zero digit
		f = 1
		while(f/d == 0):
			f *= 10

		r = f % d #r = 10 - 7 = 3
		s = np.array([r], dtype = np.int)
		print d, ": ",

		while (np.sum(s[:-1] == s[-1]) == 0 or len(s) == 1) and len(s) < d:
			r = 10*r % d
			print r,
			if r == 0:
				s = np.array([0])
				break
			s = np.append(s, r)

		if max_length < len(s) - 1:
			max_length = len(s) - 1
			d_best = d
	
		print "\ncycle length: ", len(s) - 1
	
	return max_length, d_best

if __name__ == "__main__":
	print find_largest_reciprocal_period(1000)
