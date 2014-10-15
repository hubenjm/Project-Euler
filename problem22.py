def get_names(filename):
	with open(filename) as f:
		names = f.readlines()

	names = names[0].split(",")
	return sorted([s[1:-1] for s in names])
	
def grade_word(s, j):
	c_list = list(s)
	grade = 0
	for c in c_list:
		grade += ord(c) - ord('A') + 1
	return grade*j
	
def main():
	filename = "p022_names.txt"
	names = get_names(filename)
	sum_grades = 0
	for j in range(len(names)):
		sum_grades += grade_word(names[j], j+1)
	print(sum_grades)
	
	
if __name__ == "__main__":
	main()
