months = {"Jan": 3, "Feb": 0, "Mar": 3, "Apr": 2, "May": 3, "Jun": 2, "Jul": 3, "Aug": 3, "Sept": 2, "Oct": 3, "Nov": 2, "Dec": 3}

count = 0
day = 1	# Monday is 0
for year in range(1901, 2001):
	leap = 0
	if(year % 4 == 0):
		leap = 1
	for month in months:
		if(month == "Feb"):
			day += leap
		day += months[month]
		day = day % 7
		if(day == 6):
			count += 1

print(count)