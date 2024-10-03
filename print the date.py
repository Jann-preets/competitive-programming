def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_to_date(day, year):
    months = [
        ("January", 31), ("February", 28), ("March", 31), 
        ("April", 30), ("May", 31), ("June", 30), 
        ("July", 31), ("August", 31), ("September", 30), 
        ("October", 31), ("November", 30), ("December", 31)
    ]

    if is_leap_year(year):
        months[1] = ("February", 29)

    if day < 1 or day > (366 if is_leap_year(year) else 365):
        return "Invalid day input."

    for month_name, days in months:
        if day <= days:  
            return f"{day} {month_name}, {year}"
        day -= days  

input_day = int(input())
input_year = int(input())
result = day_to_date(input_day, input_year)
print(result)  
