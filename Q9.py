x=int(input(" enter the year"))
if x%4==0 and x%100!=0 or x%400==0 :
    if x%100==0:
        print(" century leap year")

    else:
        print(" non  century leap year")
else:
    if x%100!=0 :
        print("non century non leap year")
    else:
        print("century non leap year")