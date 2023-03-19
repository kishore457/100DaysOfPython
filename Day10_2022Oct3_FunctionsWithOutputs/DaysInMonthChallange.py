def is_leap(year):
    """"this method will take year as input and true or
    false based on leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = is_leap(year)
    if leap and month == 2:
        return 29
    #   return month_days[month - 1] //it can be used used instead of elif statements.
    elif not leap and month == 2:
        return month_days[1]
    elif month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month ==10 or month == 12:
        return month_days[0]
    elif month ==4 or month ==6 or month ==9 or month == 11:
        return month_days[3]




# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







