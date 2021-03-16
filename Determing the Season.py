#Program made by Arsh Suri

#defines a class named with months with instaniates of monthindex and dayrange for a month
class months():
    def __init__(self, monthindex, dayrange):
        self.monthindex = monthindex
        self.dayrange = dayrange

#defines a function of askinput and asks the the month and day, this program only can accept the user if it types the name  of the month
def askinput():
    tempmonth = input("Enter a Month : ")

    #Validation for the user's day
    while True:
        tempday = input("Enter a Day: ")

        #Makes sure the inputted day isn't negative . Also, evalutes the user inputted string as the object of the class months and asks if the user inputted day is less than the day range for the class.
        if int(tempday) < 0 or int(tempday) > eval(tempmonth).dayrange :
            print("Make sure you type the day correctly!")
        else:
            break

    return [tempmonth, tempday]

#THe function with determines the season
def seasons(usermonth, userday):
    #evalutes the month number or which month of the year. Example, January has a month index of 1, it evalutes the string from askinput() as a class object and asks it monthindex
    usermonthindex = eval(usermonth).monthindex

    #sets the userday to concentate the strings of usermonthindex and userday. This allows for vastly simpler comparison between days and making sure  it is inside a day range.
    #WIth this system, essentially dates are represented as regular dates with no slashes. Example, January 1st or 1/21 would be 121 with the code. Since, all days are validated
    #we don't have to check for invalidated days

    #Adds the 0 before userday because single digit days would be less than dates it is not supposed to. Ex: March 5 = 35. Jan 23 = 123. 35 < 123. This error messed up the general order of dates. So we add an 0.
    if int(userday) < 10:
        userday = "0" + userday

    userdate = str(usermonthindex) + userday
    userdate = int(userdate)


    #Asks if the userdate is within the range using the new day format
    if 320 <= userdate <= 619:

        return 'Spring'
    if 620 <= userdate <= 921:

        return 'Summer'
    if 922 <= userdate <= 1220:

        return 'Fall'
    if 1221 <= userdate or userdate <= 319 :

        return 'Winter'

#instiating new class objects with monthindex and dayrange so all months are accounted for
January = months(1, 31)
February = months(2, 28)
March = months(3, 31)
April = months(4, 30)
May = months(5, 31)
June = months(6, 30)
July = months(7, 31)
August = months(8, 31)
September = months(9, 30)
October = months(10, 31)
November = months(11, 30)
December = months(12, 31)

#sets a while input and have seasons() and userinput()
while True:
    userinput = askinput()
    print("The season is " + seasons(userinput[0], userinput[1]))

    #asks if they want to continue further
    usercontinue = input("Do you want to continue? Type yes or stop : ")
    if usercontinue == "yes":
        pass
    elif usercontinue == "stop" :
        break
    else:
        print("Can you type your day again")


