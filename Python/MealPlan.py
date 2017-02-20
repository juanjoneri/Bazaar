import datetime

#change to user imput
plata = int(input("How much money do you have? >>  "))

tod = datetime.datetime.now().date()

#change to user imput
month = int(input("graduation month? [May] >> ") or "5")
day = int(input("graduation day? [6] >> ") or "6")

#shall we not count any days for some reason?
ned = int(input("any non-eating days? [0] >> ") or "0")

#usually day 6  month 5
out = datetime.date(2016, month, day)
print()
print("today: ", tod)
print("break: ",out)

print("Can spend: $", round(plata/((out-tod).days - ned), 2), "per day")
