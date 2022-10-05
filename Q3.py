x1=int(input(" enter the side "))
x2=int(input(" enter the side "))
x3=int(input("enter the side "))
match x1==x2==x3:
    case 1:
        print("sides are of equilateral traingle")

match x1!=x2!=x3:
    case 1:
        print("side are of right angle traingle")
match x1!=x2==x3 or x1==x2!=x3 or x1!=x3==x2 :
    case 1:
        print(" side of isocoles traingle  ")
 