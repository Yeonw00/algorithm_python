hour_min = input().split()

hour = int(hour_min[0])
minutes = int(hour_min[1])

if minutes - 45 < 0:
    hour -= 1
    minutes = 60 -45 + minutes
else:
    minutes -= 45

if hour < 0:
    hour = 23

print(' '.join([str(hour),str(minutes)]))