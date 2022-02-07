def building():
    width = int(input("Enter the width: "))
    length = int(input("Enter the length: "))
    depth = int(input("Enter the depth: "))

    formula = width * length * depth
    print("Total amount of concrete required is: ", formula)


building()

userinfo = input("Do you want to calculate another one?: ")
if userinfo == "y" and "Y":
    building()
else:
    exit()
