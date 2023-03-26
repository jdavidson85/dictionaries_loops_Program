def main():
    days_and_steps = {}
    total = 0
    maximum = 0
    minimum = 200000000
    print("You will be entering the date and number of steps taken for each ")
    print("day in a week.")
    for day in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",):
        steps = int(input("Please enter the number of steps taken on " + day + ": "))
        days_and_steps[day] = steps
        if steps > maximum:
            maximum = steps
        if steps < minimum:
            minimum = steps
        total += steps
    average = total/7
    print("\n\n\nYou walked a total of " + format(total, ',.0f') + "steps during the week")
    print("That was an average of " + format(average, ',.0f'))
    print("The maximum steps you took were: " + str(maximum) + " on ")
    for d in days_and_steps:
        if days_and_steps[d] == maximum:
            print("\t" + d)
    print("The minimum steps you took were: " + str(minimum) + " on ")
    for d in days_and_steps:
        if days_and_steps[d] == minimum:
            print("\t" + d)


main()
