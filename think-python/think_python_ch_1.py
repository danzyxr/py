# chapter 1

# exercise 1.3

km = 10
mi = km / 1.61

minutes = 43
seconds = 30
time_sec = (minutes * 60) + seconds
time_min = time_sec / 60
time_hrs = time_min / 60

print("Minutes per mile: " + str(time_min / mi))

print("Miles per hour: " + str(mi / time_hrs))
