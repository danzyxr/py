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
