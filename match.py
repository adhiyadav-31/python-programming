number=int(input("enter the number from 0-4:"))
match number:

    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case _:
        print("incorrect input")