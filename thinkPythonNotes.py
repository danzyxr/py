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

# chapter 2

# exercise 2.2

width = 17
height = 12.0
delimiter = '.'

print(width/2)
print(width/2.0)
print(height/3)
print(1 + 2 * 5)
print(delimiter * 5)

# exercise 2.3.1

r = 5
print((4/3)*3.14*(r**3))

# exercise 2.3.2

order_amount = 50
discount_percent = 0.4
book_price = 24.95

order_total = (book_price * discount_percent) * order_amount
shipping_cost = 3 + (.75 * (order_amount - 1))
grand_total = order_total + shipping_cost
print(f"Grand total: {grand_total}")

# exercise 2.3.3

clock_hour = 6
clock_mins = 52
clock_secs = 0
total_secs = (clock_hour * 3600) + (clock_mins * 60)

slow = (8 * 60) + 15
fast = (7 * 60) + 12

total_secs += (slow * 2) + (fast * 3)

clock_hour = total_secs // 3600
clock_mins = (total_secs % 3600) // 60
clock_secs = int((((total_secs % 3600) / 60) % 1) * 60)

print(f"Clock hour is {clock_hour}")
print(f"Clock mins is {clock_mins}")
print(f"Clock secs is {clock_secs}")
