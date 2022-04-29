#! python3
# lockBruteForce.Simplex.L1021B.Simple.py -v 1.0
# Author- David Sullivan
#
# Rules:
#   - 5 buttons on lock
#   - 2 buttons can be pressed simultaneously to create a new digit
#   - PIN length can be from 1 to 5 digits
#   - buttons cannot be used twice
#   - 1 second per PIN

from itertools import chain


def digitCalculation():
    # list of starting digits
    digits = [1, 2, 3, 4, 5]

    # calculate all potential digits
    for i in range(5):
        # loop through numbers to determine 2 button press digits
        for i2 in range(5):
            # check to see if numbers are different
            if i != i2:
                # create button combo
                combo = [i + 1]
                combo.append(i2 + 1)
                combo.sort()
                # if numbers are different, check for unique button combo
                if combo not in digits:
                    # if unique, add to button combo list and add new digit
                    digits.append(combo)
    return digits


def oneDigitPIN(digits):
    p1_list = []
    # loop through all digits for first number
    for n1 in range(len(digits)):
        # add PIN length 1 combo to p1 variable and total combos
        p1_list.append(digits[n1])
    return p1_list


def twoDigitPIN(digits):
    p2_list = []
    # loop through all digits for each number
    for n1 in range(len(digits)):
        for n2 in range(len(digits)):
            # check to see if number repeats
            if digits[n1] != digits[n2]:
                if type(digits[n1]) is list:
                    if type(digits[n2]) is list:
                        if len(list(set(digits[n1]) & set(digits[n2]))) == 0:
                            p2_list = addTwo(digits[n1], digits[n2], p2_list)
                        else:
                            pass
                    elif digits[n2] not in digits[n1]:
                        p2_list = addTwo(digits[n1], digits[n2], p2_list)
                elif type(digits[n1]) is not list:
                    if type(digits[n2]) is list:
                        if digits[n1] not in digits[n2]:
                            p2_list = addTwo(digits[n1], digits[n2], p2_list)
                        else:
                            pass
                    else:
                        p2_list = addTwo(digits[n1], digits[n2], p2_list)
    return p2_list


def threeDigitPIN(digits):
    p3_list = []
    # loop through all digits for each number
    for n1 in range(len(digits)):
        for n2 in range(len(digits)):
            # check to see if number is already used
            if digits[n1] != digits[n2]:
                for n3 in range(len(digits)):
                    # check to see if number is already used
                    if digits[n1] != digits[n3] and digits[n2] != digits[n3]:
                        # check to see if first digit is more than one button
                        if type(digits[n1]) is list:
                            # check to see if second digit is more than one button
                            if type(digits[n2]) is list:
                                # check to see if third digit is more than one button
                                if type(digits[n3]) is list:
                                    # too many numbers, combination cannot be used
                                    pass
                                else:
                                    # digits 1 and 2 buttons are 2 buttons, digit 3 is 1 button
                                    if len(list(set(digits[n1]) & set(digits[n2]))) == 0:
                                        if digits[n3] in digits[n1] or digits[n3] in digits[n2]:
                                            pass
                                        else:
                                            p3_list = addThree(digits[n1], digits[n2], digits[n3], p3_list)
                                    else:
                                        pass
                            else:
                                # check to see if third digit is more than one button
                                if type(digits[n3]) is list:
                                    # digits 1 and 2 are 1 button, digit 3 is 2 buttons
                                    if digits[n2] in digits[n1] or digits[n2] in digits[n3]:
                                        pass
                                    else:
                                        p3_list = addThree(digits[n1], digits[n2], digits[n3], p3_list)
                                else:
                                    # all digits are 1 button
                                    if digits[n2] in digits[n1] or digits[n3] in digits[n1]:
                                        pass
                                    else:
                                        p3_list = addThree(digits[n1], digits[n2], digits[n3], p3_list)
                        else:
                            # digit 1 is one button, now check buttons 2 and 3
                            if type(digits[n2]) is list:
                                # check to see if third digit is more than one button
                                if type(digits[n3]) is list:
                                    # digit 1 is 1 button, digits 2 and 3 are 2 buttons
                                    if len(list(set(digits[n2]) & set(digits[n3]))) == 0:
                                        if digits[n1] in digits[n2] or digits[n1] in digits[n3]:
                                            pass
                                        else:
                                            p3_list = addThree(digits[n1], digits[n2], digits[n3], p3_list)
                                    else:
                                        pass
                                else:
                                    # digits 1 and 3 are 1 button, digit 2 is 2 buttons
                                    if digits[n1] in digits[n2] or digits[n3] in digits[n2]:
                                        pass
                                    else:
                                        p3_list = addThree(digits[n1], digits[n2], digits[n3], p3_list)
                            else:
                                # digits 1 and 2 are 1 button, check digit 3
                                if type(digits[n3]) is list:
                                    # digits 1 and 2 are 1 button, digit 3 is 2 buttons
                                    if digits[n1] in digits[n3] or digits[n2] in digits[n3]:
                                        pass
                                    else:
                                        p3_list = addThree(digits[n1], digits[n2], digits[n3], p3_list)
                                else:
                                    # all three digits are 1 button, none are duplicates
                                    p3_list = addThree(digits[n1], digits[n2], digits[n3], p3_list)
    return p3_list


def fourDigitPIN(digits):
    p4_list = []
    # loop through all digits for each number, there can only be at most 1 digit that uses 2 buttons
    for n1 in range(len(digits)):
        for n2 in range(len(digits)):
            # check to see if number is already used
            if digits[n1] != digits[n2]:
                for n3 in range(len(digits)):
                    # check to see if number is already used
                    if digits[n1] != digits[n3] and digits[n2] != digits[n3]:
                        for n4 in range(len(digits)):
                            # check to see if number is already used
                            if digits[n1] != digits[n4] and digits[n2] != digits[n4] and digits[n3] != digits[n4]:
                                # check to see if first digit is more than one button
                                if type(digits[n1]) is list:
                                    # check to see if second digit is more than one button
                                    if type(digits[n2]) is list:
                                        # too many numbers, combination cannot be used
                                        pass
                                    else:
                                        # check to see if third digit is more than one button
                                        if type(digits[n3]) is list:
                                            # too many numbers, combination cannot be used
                                            pass
                                        else:
                                            # check to see if fourth digit is more than one button
                                            if type(digits[n4]) is list:
                                                # too many numbers, combination cannot be used
                                                pass
                                            else:
                                                # digit 1 is 2 buttons- 2,3, and 4 are all 1 button
                                                if digits[n2] in digits[n1] or digits[n3] in digits[n1] or digits[n4] in \
                                                        digits[n1]:
                                                    pass
                                                else:
                                                    p4_list = addFour(digits[n1], digits[n2], digits[n3], digits[n4],
                                                                      p4_list)
                                else:
                                    # digit 1 is one button, now check digits 2, 3, and 4
                                    if type(digits[n2]) is list:
                                        # check to see if third digit is more than one button
                                        if type(digits[n3]) is list:
                                            # too many numbers, combination cannot be used
                                            pass
                                        else:
                                            # check to see if fourth digit is more than one button
                                            if type(digits[n4]) is list:
                                                # too many numbers, combination cannot be used
                                                pass
                                            else:
                                                # digit 2 is 2 buttons- 1,3, and 4 are all 1 button
                                                if digits[n1] in digits[n2] or digits[n3] in digits[n2] or digits[n4] in \
                                                        digits[n2]:
                                                    pass
                                                else:
                                                    p4_list = addFour(digits[n1], digits[n2], digits[n3], digits[n4],
                                                                      p4_list)
                                    else:
                                        # digits 1 and 2 are one button, now check digits 3 and 4
                                        if type(digits[n3]) is list:
                                            # check to see if fourth digit is more than one button
                                            if type(digits[n4]) is list:
                                                # too many numbers, combination cannot be used
                                                pass
                                            else:
                                                # digit 3 is 2 buttons- 1,2, and 4 are all 1 button
                                                if digits[n1] in digits[n3] or digits[n2] in digits[n3] or digits[n4] in \
                                                        digits[n3]:
                                                    pass
                                                else:
                                                    p4_list = addFour(digits[n1], digits[n2], digits[n3], digits[n4],
                                                                      p4_list)
                                        else:
                                            # digits 1, 2, and 3 are one button, now check digit 4
                                            if type(digits[n4]) is list:
                                                # digit 4 is 2 buttons- 1,2, and 3 are all 1 button
                                                if digits[n1] in digits[n4] or digits[n2] in digits[n4] or digits[
                                                    n3] in digits[n4]:
                                                    pass
                                                else:
                                                    p4_list = addFour(digits[n1], digits[n2], digits[n3], digits[n4],
                                                                      p4_list)
                                            else:
                                                # all four digits are 1 button, none are duplicates
                                                p4_list = addFour(digits[n1], digits[n2], digits[n3], digits[n4],
                                                                  p4_list)
    return p4_list


def fiveDigitPIN(digits):
    p5_list = []
    # loop through all digits for each number, no digits can use 2 buttons, we only need to use single buttons here
    for n1 in range(1, 6):
        for n2 in range(1, 6):
            # check to see if number is already used
            if digits[n1] != digits[n2]:
                for n3 in range(1, 6):
                    # check to see if number is already used
                    if digits[n1] != digits[n3] and digits[n2] != digits[n3]:
                        for n4 in range(1, 6):
                            # check to see if number is already used
                            if digits[n1] != digits[n4] and digits[n2] != digits[n4] and digits[n3] != digits[n4]:
                                for n5 in range(1, 6):
                                    # check to see if number is already used
                                    if digits[n1] != digits[n5] and digits[n2] != digits[n5] and digits[n3] != digits[
                                        n5] and digits[n4] != digits[n5]:
                                        # no numbers have been repeated, add to list
                                        p5_list = addFive(digits[n1], digits[n2], digits[n3], digits[n4], digits[n5],
                                                          p5_list)
    return p5_list


def addTwo(n1, n2, p2_list):
    templist = [n1, n2]
    p2_list.append(templist)
    return p2_list


def addThree(n1, n2, n3, p3_list):
    templist = [n1, n2, n3]
    p3_list.append(templist)
    return p3_list


def addFour(n1, n2, n3, n4, p4_list):
    templist = [n1, n2, n3, n4]
    p4_list.append(templist)
    return p4_list


def addFive(n1, n2, n3, n4, n5, p5_list):
    templist = [n1, n2, n3, n4, n5]
    p5_list.append(templist)
    return p5_list


def timeCalc(combos):
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
        time_left = time_left - (weeks * week)

    # calculate days
    if day <= time_left:
        days = int(time_left / day)
        time_left = time_left - (days * day)

    # calculate hours
    if hour <= time_left:
        hours = int(time_left / hour)
        time_left = time_left - (hours * hour)

    # calculate minutes
    if minute <= time_left:
        minutes = int(time_left / minute)
        seconds = time_left - (minutes * minute)

    return weeks, days, hours, minutes, seconds


def results(digits, p1, p2, p3, p4, p5, combos):
    print("Total digits: " + str(len(digits)))
    print("------------------------------------------------")
    print("PIN length 1 combinations: " + str(len(p1)))
    print("PIN length 2 combinations: " + str(len(p2)))
    print("PIN length 3 combinations: " + str(len(p3)))
    print("PIN length 4 combinations: " + str(len(p4)))
    print("PIN length 5 combinations: " + str(len(p5)))
    print("------------------------------------------------")
    print("Total combinations: " + str(combos))
    print("------------------------------------------------")
    print("------------------------------------------------")

    # run module to calculate time required
    weeks, days, hours, minutes, seconds = timeCalc(combos)

    print("Time Required:")
    print("------------------------------------------------")
    print("Weeks: " + str(weeks))
    print("Days: " + str(days))
    print("Hours: " + str(hours))
    print("Minutes: " + str(minutes))
    print("Seconds: " + str(seconds))
    print("------------------------------------------------")


if __name__ == '__main__':
    # run digits module
    digits = digitCalculation()

    # run modules for each PIN length
    p1_list = oneDigitPIN(digits)
    p2_list = twoDigitPIN(digits)
    p3_list = threeDigitPIN(digits)
    p4_list = fourDigitPIN(digits)
    p5_list = fiveDigitPIN(digits)

    # add results together
    combos = len(p1_list) + len(p2_list) + len(p3_list) + len(p4_list) + len(p5_list)
    brute_combos = list(chain(p1_list, p2_list, p3_list, p4_list, p5_list))

    # run results page
    results(digits, p1_list, p2_list, p3_list, p4_list, p5_list, combos)
