def building():
    buildingtype = input("Building type (Commerical / residential): ")
    length = int(input("Length: "))
    width = int(input("Width: "))
    depth = int(input("Depth: "))
    formula = length * width * depth
    print("Building Type: ")
    print("You need ", formula, " volume of concrete ")

building()