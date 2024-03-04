def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else :
        return False


year = 2004 
result = is_leap_year(year)
print(result)       



year = int(input ("enter year"))
if year % 4 == 0  and year % 100 != 0 or year % 400 == 0:
    print(year, "is leap year")
else :
    print(year ,"is not leap year")  