from T006_P4_booksUI import case1, case2, case3, case4

cmnd = input("Enter the case you want to run (1, 2, 3, 4)")
while cmnd != "1" and cmnd != "2" and cmnd != "3" and cmnd != "4":
    cmnd = input("Enter the case you want to run (1, 2, 3, 4)")
if cmnd == "1":
    case1()
elif cmnd == "2":
    case2()
elif cmnd == "3":
    case3()
elif cmnd == "4":
    case4()
else:
    cmnd == input("Enter the case you want to run (1, 2, 3, 4)")