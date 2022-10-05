s1=str(input("enter the first string"))
s2=str(input("enter the second string"))
match s1==s2:
    case 1:
        print("both string are identical")
match s1>s2:
    case 1:
        print("string  first come before string second")
match s2>s1:
    case 1 :
        print("string second come before string first ")
