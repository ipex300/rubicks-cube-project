for xb in range(3):
    """case8"""

    if cube[y][8] == "W":
        count = 0

        if cube[y][8] != "W" or cube[z][4] != cube[z][6] or cube[5][3] != cube[y][4]:
            continu = 1
        while continu:
            y += 1
            z += 1
            if cube[y][8] == "W":
                move_D1()
                if cube[z][6] == cube[z][4]:
                    if cube[5][3] == cube[y][4]:
                        print("8 CASe")
                        move_D2()
                        list_of_movement2[z]()
                        move_D1()
                        list_of_movement1[z]()
                        continu = 0

    """case6"""
    if cube[y][6] == "W":
        count = 1
        print("6CASE")
        while cube[y][6] != "W" and cube[x][4] != cube[x][6] and cube[5][1] != cube[y][4]:
            if count == 4:
                break
            move_D2()
            if cube[y][6] == "W":
                if cube[x][4] == cube[x][6]:
                    if cube[5][1] == cube[y][4]:
                        print("6CASE")
                        move_D1()
                        list_of_movement1[x]()
                        move_D2()
                        list_of_movement2[x]()
                        if count == 4:
                            break

    """case0"""
    if cube[y][0] == "W":
        list_of_movement2[y]()
        move_D1()
        move_D1()
        list_of_movement1[y]()
    """case2"""
    if cube[y][2] == "W":
        list_of_movement1[y]()
        move_D2()
        move_D2()
        list_of_movement2[y]()
        print("case2")

