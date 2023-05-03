def is_leap_year(year):
    """
    Returns True if the given year is a leap year, and False otherwise.
    """
    if year % 4 != 0:
        # If the year is not divisible by 4, it's not a leap year
        return False
    elif year % 100 != 0:
        # If the year is divisible by 4 but not by 100, it's a leap year
        return True
    elif year % 400 != 0:
        # If the year is divisible by 100 but not by 400, it's not a leap year
        return False
    else:
        # If the year is divisible by both 100 and 400, it's a leap year
        return True


print(is_leap_year(2004))
