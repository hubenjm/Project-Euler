import numpy as np

#reference: january 1, 1900 was a Monday

def compute_start_day(year):
	#0 is sunday, 6 is saturday

	s1 = sum([31,28,31,30,31,30,31,31,30,31,30,31]) % 7
	s2 = sum([31,29,31,30,31,30,31,31,30,31,30,31]) % 7

	day_offset = 0

	if year < 1900:
		for j in xrange(year, 1900):
			if (j % 4 == 0 and j % 100 != 0) or j % 400 == 0:
				day_offset += s2
			else:
				day_offset += s1

		return (1-day_offset)%7

	else:
		for j in xrange(1900, year):
			if (j % 4 == 0 and j % 100 != 0) or j % 400 == 0:
				day_offset += s2
			else:
				day_offset += s1
		
		return (1 + day_offset)%7

def count_sundays(year1, year2):
	assert year1 < year2
	
	current_year_jan_1 = compute_start_day(year1)
	num_sundays = 1*(current_year_jan_1 == 0)
	print current_year_jan_1

	for y in xrange(year1, year2 + 1):
		if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
			days_in_month = np.array([31,29,31,30,31,30,31,31,30,31,30,31], dtype = np.int)
		else:
			days_in_month = np.array([31,28,31,30,31,30,31,31,30,31,30,31], dtype = np.int)

		num_sundays += np.sum( np.mod(np.cumsum(days_in_month) + current_year_jan_1, 7) == 0 )
		print y, np.mod(np.cumsum(days_in_month) + current_year_jan_1, 7)
		current_year_jan_1 = (np.sum(days_in_month) + current_year_jan_1) % 7

	if current_year_jan_1 % 7 == 0:
		num_sundays -= 1 #only want to count from jan 1, year1 to dec 31, year2

	return num_sundays


def main():
	year1 = 1901
	year2 = 2000
	print count_sundays(year1, year2)

if __name__ == "__main__":
	main()		
