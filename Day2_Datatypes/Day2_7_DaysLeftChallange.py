age = input("what is your age : ")

int_age = int(age)

years_remaining = 90 - int_age

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"you have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months")