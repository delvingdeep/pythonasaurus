"""
This function calculates number of week it will take for entered days
It also return the number days left along with the excat count
"""

def readable_timedelta(days):
    weeks = int(days//7)
    day_minus_week = int(days%7)
    week = str(weeks)
    day = str(day_minus_week)
    output = ("{} week(s) and {} day(s)".format(week, day))
    return output

# On calling the function, we get exact count
print(readable_timedelta(10))
