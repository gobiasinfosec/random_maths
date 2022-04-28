#! python3
# lockBruteForce.py -v 1.0
# Author- David Sullivan
#
# Rules:
#   - 5 numbers on lock
#   - 2 numbers can be pressed simultaneously to create a new number
#   - PIN length can be from 1 to 5 digits
#   - numbers cannot repeat in PIN
#   - 1 second per PIN

# setup digits variable
digits = 0

# numbers on lock
numbers = [1, 2, 3, 4, 5]

# create empty list to compare 2 button press
b2 = []

# calculate potential digits
for i in range(len(numbers)):
    # add single digit numbers to digits total
    digits += 1
    # loop through numbers to determine 2 button press digits
    for i2 in range(len(numbers)):
        # check to see if numbers are different
        if i != i2:
            # create button combo
            combo = [i]
            combo.append(i2)
            combo.sort()
            # if numbers are different, check for unique button combo
            if combo not in b2:
                # if unique, add to button combo list and add new digit
                b2.append(combo)
                digits += 1

# setup combinations variable
combos = 0

# setup variables for total pin length
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

# loop through all digits for first number
for i1 in range(digits):
    # add PIN length 1 combo to p1 variable and total combos
    p1 += 1
    combos += 1
    # loop through all digits for second number
    for i2 in range(digits):
        # check to see if number repeats
        if i1 != i2:
            # if it doesn't repeat, add to p2 variable and total combos
            p2 += 1
            combos += 1
            # loop through all digits for third number
            for i3 in range(digits):
                # check to see if number repeats
                if i2 != i3:
                    # if it doesn't repeat, add to p3 variable and total combos
                    p3 += 1
                    combos += 1
                    # loop through all digits for fourth number
                    for i4 in range(digits):
                        # check to see if number repeats
                        if i3 != i4:
                            # if it doesn't repeat, add to p4 variable and total combos
                            p4 += 1
                            combos += 1
                            # loop through all digits for fourth number
                            for i5 in range(digits):
                                # check to see if number repeats
                                if i4 != i5:
                                    # if it doesn't repeat, add to p5 variable and total combos
                                    p5 += 1
                                    combos += 1

# time in seconds
minute = 60
hour = minute * 60
day = hour * 24
week = day * 7

# setup variables for time
time_left = combos
seconds = 0
minutes = 0
hours = 0
days = 0
weeks = 0

# calculate weeks
if week <= time_left:
    weeks = int(time_left / week)
    # determine time left
    time_left = time_left - (weeks * week)

# calculate days
if day <= time_left:
    days = int(time_left / day)
    # determine time left
    time_left = time_left - (days * day)

# calculate hours
if hour <= time_left:
    hours = int(time_left / hour)
    # determine time left
    time_left = time_left - (hours * hour)

# calculate minutes
if minute <= time_left:
    minutes = int(time_left / minute)
    # determine time left as seconds
    seconds = time_left - (minutes * minute)

# print variables
print("Total digits: " + str(digits))
print("PIN length 1 combinations: " + str(p1))
print("PIN length 2 combinations: " + str(p2))
print("PIN length 3 combinations: " + str(p3))
print("PIN length 4 combinations: " + str(p4))
print("PIN length 5 combinations: " + str(p5))
print("Total combinations: " + str(combos))
print("Time Required:")
print("Weeks: " + str(weeks))
print("Days: " + str(days))
print("Hours: " + str(hours))
print("Minutes: " + str(minutes))
print("Seconds: " + str(seconds))
