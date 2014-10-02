import time
from math import ceil, log10

def get_numbers():
	"""
	Returns list of numbers in data file
	"""
	filename = "problem13-data.txt"
	text_file = open(filename, "r")
	lines = text_file.readlines()
	text_file.close()
	L = [int(lines[i]) for i in range(len(lines))]
	return L
	
def test():
	L = get_numbers()
	print(L[0])
	
def main():
	start = time.time()
	L = get_numbers()
	S = sum(L)
	ndigits = int(ceil(log10(S)))
	S_red = (S - S%10**(ndigits-10))/10**(ndigits-10)
	print(S_red)
	end = time.time()
	print(end-start)
	
if __name__ == "__main__":
	main()
