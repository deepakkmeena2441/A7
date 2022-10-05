s=str(input("enter the  string"))
c=len(s)
match c:
    case 1:
        print(" single word string")
    case _:
        print(" multi word string")
    
