def isLeap(year):
	if (year % 100 != 0):
		if (year % 4 == 0):
			result = True
		else:
			result = False
	else:
		if ((year //100) % 4 == 0):
			result = True
		else:
			result = False
	return result