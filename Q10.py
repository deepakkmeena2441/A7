x=eval(input(" enter the colour"))
match x:
    case "yellow":
        print(" day is monday")
    case "blue":
        print(" day is tuesday")
    case "orange" :
        print("day is wednesday")
           
    case "white":
        print("day is thursday")
    case "black":
        print(" day is friday")
    case " red":
        print(" day is saturday")
    case _:
        print(" day is sunday")