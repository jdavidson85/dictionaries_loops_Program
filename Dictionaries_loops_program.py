days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
for i in range(len(days)):
    s = int(input("Please enter the number of steps taken on " + days[i] + ": "))
    steps.append(s)
print("\n\n\nYou walked a total of " + str(sum(steps))+" steps during the week.\nThat was an average of "
      + str(int((sum(steps)/len(steps)))))
for i in range(len(steps)):
    if steps[i] == max(steps):
        print("The maximum steps you took were: " + str(steps[i])+" on " + days[i])
for i in range(len(steps)):
    if steps[i] == min(steps):
        print("The minimum steps you took were: " + str(steps[i])+" on " + days[i])
