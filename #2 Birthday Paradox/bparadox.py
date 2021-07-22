import random

def getbdays(num):
    thecalendar = {'Jan':32, 'Feb':29, 'Mar':32, 'Apr':31, 'May':32, 'Jun':31, 'Jul':32, 'Aug':32, 'Sep':31, 'Oct':32, 'Nov':31, 'Dec':32}
    months = list(thecalendar.keys())
    bdays = []
    for i in range(num):
        randmonth = random.choice(months)
        randdate = random.randrange(1,thecalendar[randmonth])
        randbday = randmonth+' '+str(randdate)
        bdays.append(randbday)
    return bdays

num = int(input("How many birthdays shall I generate? (Max 100)\n>"))

bdays = getbdays(num)

print("Here are {} birthdays in a list:".format(num))
print(bdays)