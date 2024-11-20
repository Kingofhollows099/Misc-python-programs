try:
    time = 0
    askDays = 1
    while True:
        if askDays == 1:
            dayTime = int(input("Days: ")) * 24 * 60
            time += dayTime
            if dayTime == 0:
                askDays = 0
        time += int(input("Hours: ")) * 60
        time += int(input("Minutes: "))
except:
    hours, minutes = divmod(time, 60)
    print(f"Small measurments: {hours} Hours, and {minutes} minutes")

    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    print(f"Total: {weeks} weeks, {days} days, {hours} hours, and {minutes} minutes.")