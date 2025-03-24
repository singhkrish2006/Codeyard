n=int(input(“ Enter year 4 digit form “))
if n % 100==0:
    if n % 400 ==0:
        print(“ Leap Year“)
    else:
        print(“ Not a leap year“)
else:
    if y % 4==0:
        print(“ Leap Year“)
    else:
        print(“ Not a leap year“)
