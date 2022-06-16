def leap_year(year):
    """
    :description: Program to ensure it is a 4-digit number. Determine if it is a Leap Year.
    :param year: year
    :return: year
    """
    # Ensuring year is 4-digit number
    if 1000 <= year <= 9999:

        # To check if year is leap year or not
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(year, "is Leap Year ")
        else:
            print(year, "is Not Leap Year")
    else:
        print("Enter valid Year")
    return year



if __name__ == '__main__':
    year = int(input("Enter the Year : "))
    leap_year(year)