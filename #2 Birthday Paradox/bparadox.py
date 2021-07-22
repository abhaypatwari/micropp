import random
from collections import Counter

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
print("Here are {} random birthdays in a list:".format(num))
print(bdays)

repeats = Counter(bdays)
same = [repeat for repeat in repeats if repeats[repeat]>1]
print("\nIn this simulation, multiple people have a birthday on the following dates:")
print(same)

input("\nNow Imma run this simulation 100,000 times...\nPress Enter to begin...")
match=0
for numsim in range(1,100001):
    bdays = getbdays(num)
    repeats = Counter(bdays)
    same = [repeat for repeat in repeats if repeats[repeat]>1]
    match+=len(same)
    if(numsim%10000==0):
        print("{} simulations run...".format(numsim))

probability = match/100000
print("Out of 100,000 simulations of {} people,\nthere was a matching birthday {} times.".format(num,match))
print("Hence probability of 2 people sharing a birthday in a group of {} people is {}%".format(num,probability*100))