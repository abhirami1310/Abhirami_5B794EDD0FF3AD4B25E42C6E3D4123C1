#leap year

"""
year% 4==0 &
year% 100!= /
year% 400==0

"""
def isLeapyear(year):
 if (year % 4==0 and year % 100!=0) or year % 400==0:
    return True
 else:
    return False

year=2010

if isLeapyear (year):
 print("{} is a leapyear.".format(year))
else:
 print("{} is not a leapyear.".format(year))

       