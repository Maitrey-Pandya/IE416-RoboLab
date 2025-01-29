def no_of_days(year):    
    if (year<0):
        print("Please enter valid year !")
    else:
        if (year%4==0):
            if (year%100==0):
                if (year%400==0):
                    print(366)
                else:
                    print(365)
            else:
                print(366)
        else:
            print(365)
    return 0
year=int(input("Enter the year :"))
no_of_days(year)
