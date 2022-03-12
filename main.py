from termcolor import colored

run = True

while run:
    print(colored("-------------- Down below 2 programs that tells-------------------\n","blue"))
    print(colored("1. Check whether its leap year or not\n","green"))
    print(colored("2. How many leap year in Given date and what are they?","yellow"))
    run1 = True
    while run1:
        inpt =input("Enter: ")
        leap_year = []
        exp_leapyear = []
        def check_leapyear(inp = 0):
            if inp%400==0 or (inp%4==0 and inp % 100 !=0):
                return True

            return False

        def list_leapyear(leap_year_till_date):
            i = 4
            while i<=leap_year_till_date:
                if i%400==0 or (i%4==0 and i%100!=0):
                    leap_year.append(i)
                else:
                    exp_leapyear.append(i)
                i+=1

        if inpt == "1":
            inp = int(input("Enter year to check: "))
            if check_leapyear(inp):
                print(f"Yes, the {colored(inp, 'yellow')} year is leap year.")
                run1 = False
            else:
                print(f"No, the {colored(inp, 'red')} year is not leap year.")
                run1 = False

        elif inpt == "2":
            leap_year_till_date = int(input("Enter year: "))
            list_leapyear(leap_year_till_date)
            result = "There are {:,} leap year."
            # print(f"There are {len(leap_year)} leap year.")
            print(result.format(len(leap_year)))
            want_run = True
            while want_run:
                want = input("Want to see what are they? Y/N: ").upper()
                if want == "Y":
                    for i in leap_year:
                        print(i)
                        want_run = False
                elif want == "N":
                    print(colored("------ Thank You -------","green"))
                    want_run = False

                else:
                    print(colored("Invalid Entry, please type Y/N.","red"))
            run1 = False
        else:
            print(colored("Please enter valid number 1 or 2 ","red"))


