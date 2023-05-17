#match case same as switch case in c
x=int(input("enter thr value of x"))
match x:
    case 0:
        print("the x is zero")
    case 4:
        print("the x is four")
    case _:
        print(x)        