datafile1 = "./problem18data.txt"
datafile2 = "./problem67data.txt"

def getdata(filename):
	l = []
	with open(filename, 'r') as f:
		for line in f:
			row = [int(s.strip()) for s in line.split(" ")]
			l.append(row)

	return l

def read_data_test():
	l = getdata(datafile)
	print l

def longest_path(filename):
	l = getdata(filename)
	m = len(l)
	longest = l[0]
	longest_next = []

	for j in xrange(1,m):
		#j corresponds to level we are computing longest paths for, j = 0 corresponds to first level
		longest_next = []
		longest_next.append(l[j][0] + longest[0])
		for k in xrange(1,j):
			#cycle through the elements of level j+1 and compute longest path to that element using the longest path lengths to the elements of previous level
			longest_next.append(l[j][k] + max(longest[k-1], longest[k]))

		longest_next.append(l[j][-1] + longest[-1])
		longest = longest_next

	return max(longest)

if __name__=="__main__":
	print longest_path(datafile1)
	print longest_path(datafile2)
		
	
	
