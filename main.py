# représentation du cube
cube = [
    ['W', 'W', 'W',
     'W', 'W', 'W',
     'W', 'W', 'W'],  # Face blanche

    ['R', 'R', 'R',
     'R', 'R', 'R',
     'R', 'R', 'R'],  # Face rouge

    ['B', 'B', 'B',
     'B', 'B', 'B',
     'B', 'B', 'B'],  # Face bleue

    ['O', 'O', 'O',
     'O', 'O', 'O',
     'O', 'O', 'O'],  # Face orange

    ['G', 'G', 'G',
     'G', 'G', 'G',
     'G', 'G', 'G'],  # Face verte

    ['Y', 'Y', 'Y',
     'Y', 'Y', 'Y',
     'Y', 'Y', 'Y']]  # Face jaune

save= cube
#codage de la fonction daffichage des differente face de maniere ordonne

# codage des  différents mouvement du cube
def rotate_face_clockwise(face):
    cube[cube.index(face)]= [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

# Rotation d'une face dans le sens anti-horaire
def rotate_face_anticlockwise(face):
    cube[cube.index(face)]=  [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]

# movement up sens horaire
def move_U1() :
    initial_segment= cube[1][0:3]
    cube[1][0:3] = cube[2][0:3]
    cube[2][0:3] = cube[3][0:3]
    cube[3][0:3] = cube[4][0:3]
    cube[4][0:3] =initial_segment
    rotate_face_clockwise(cube[0])
    return cube

# mouvement up sens anti horaire
def move_U2() :
    initial_segment = cube[4][0:3]       # pour comprendre le code il faut consisdere
    cube[4][0:3] = cube[3][0:3]          # que le haut du cube cest la face blanche
    cube[3][0:3] = cube[2][0:3]           # et la partie en face de nous cest la face verte
    cube[2][0:3] = cube[1][0:3]
    cube[1][0:3] = initial_segment
    rotate_face_anticlockwise(cube[0])
# movement down sens horaire
def move_D1() :
    initial_segment = cube[3][6:9]
    cube[3][6:9] = cube[2][6:9]
    cube[2][6:9] = cube[1][6:9]
    cube[1][6:9] = cube[4][6:9]
    cube[4][6:9] = initial_segment
    rotate_face_clockwise(cube[5])
    return cube

# mouvement down sens anti horaire
def move_D2() :
    initial_segment = cube[2][6:9]
    cube[2][6:9] = cube[3][6:9]
    cube[3][6:9] = cube[4][6:9]
    cube[4][6:9] = cube[1][6:9]
    cube[1][6:9] = initial_segment
    rotate_face_anticlockwise(cube[5])
    return cube
# mouvement front sens horaire

def move_F1() :
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[0][6:9]
    cube[0][6:9] = cube[3][2:9][::-3]
    cube[3][2:9:3]= cube[5][0:3]
    cube[5][0:3] = initial_segment[::-1]
    rotate_face_clockwise(cube[4])
    return cube
# mouvement front sens anti horaire
def move_F2() :
    initial_segment = cube[1][::3]
    cube[1][::3] = cube[5][0:3][::-1]
    cube[5][0:3] = cube[3][2:9][::3]
    cube[3][2:9:3]= cube[0][6:9]
    cube[0][6:9] = initial_segment
    rotate_face_anticlockwise(cube[4])
    return cube
def move_B1():
    initial_segment = cube[3][::3]
    cube[3][::3] = cube[0][0:3][::-1]
    cube[0][0:3] = cube[1][2:9][::3]
    cube[1][2:9:3]= cube[5][6:9][::-1]
    cube[5][6:9] = initial_segment[::1]
    rotate_face_clockwise(cube[2])
    return cube
def move_B2():
    initial_segment = cube[1][2:9][::3]
    cube[1][2:9:3] = cube[0][0:3]
    cube[0][0:3] = cube[3][::3][::-1]
    cube[3][::3] = cube[5][6:9]
    cube[5][6:9] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[2])
    return cube
def move_R1():
    initial_segment =  cube[0][2:9:3]
    cube[0][2:9:3]=  cube[4][2:9:3]
    cube[4][2:9:3]= cube[5][2:9:3]
    cube[5][2:9:3]= cube[2][::3][::-1]
    cube[2][::3]= initial_segment[::-1]
    rotate_face_clockwise(cube[1])

    return cube
def move_R2():
    initial_segment = cube[2][::3]
    cube[2][::3]= cube[5][2:9:3][::-1]
    cube[5][2:9:3] = cube[4][2:9:3]
    cube[4][2:9:3] = cube[0][2:9:3]
    cube[0][2:9:3] = initial_segment[::-1]
    rotate_face_anticlockwise(cube[1])
    return cube
def move_L1():
    initial_segment =  cube[5][::3]
    cube[5][::3]= cube[4][::3]
    cube[4][::3]= cube[0][::3]
    cube[0][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3]= initial_segment[::-1]
    rotate_face_clockwise(cube[3])
    return cube
def move_L2():
    initial_segment = cube[4][::3]
    cube[4][::3] = cube[5][::3]
    cube[5][::3] = cube[2][2:9:3][::-1]
    cube[2][2:9:3] = cube[0][::3][::-1]
    cube[0][::3] = initial_segment
    rotate_face_anticlockwise(cube[3])
def cube_sloved ():
    cubes= [
    ['W', 'W', 'W',
     'W', 'W', 'W',
     'W', 'W', 'W'],  # Face blanche

    ['R', 'R', 'R',
     'R', 'R', 'R',
     'R', 'R', 'R'],  # Face rouge

    ['B', 'B', 'B',
     'B', 'B', 'B',
     'B', 'B', 'B'],  # Face bleue

    ['O', 'O', 'O',
     'O', 'O', 'O',
     'O', 'O', 'O'],  # Face orange

    ['G', 'G', 'G',
     'G', 'G', 'G',
     'G', 'G', 'G'],  # Face verte

    ['Y', 'Y', 'Y',
     'Y', 'Y', 'Y',
     'Y', 'Y', 'Y']]  # Face j
    if cube== cubes:
        return True
    else:
        return  False

from move import *
file= open("reflexion_croix.txt","r+")
y= 0
list_of_movement1= [move_U1,move_R1,move_B1,move_L1,move_F1,move_B1]
list_of_movement2= [move_U2,move_R2,move_B2,move_L2,move_F2,move_B2]
def print_cube(cube):
    for face in cube:
        for x in range(0,9,3):
            print(face[x:x+3])
        print("")
def white_cross():
    x = 0
    global y
    while cube[0][1] != "W" or cube[0][3] != "W" or cube[0][5] != "W" or cube[0][7] != "W":
        #case1 the eges are in the green face
        if cube[4][3]== "W"  :
            if cube[0][3] != "W":
                move_L2()
                y+=1
            else:
                while cube[0][3]== "W":
                    move_U1()
                    y += 1
                move_L2()
                y += 1
        if cube[4][5] == "W":
            if cube[0][5] != "W":
                move_R1()
                y += 1
            else:
                while cube[0][5] == "W":
                    move_U1()
                    y += 1
                move_R1()
                y += 1
        if cube[4][1] == "W":
            move_F1()
            y += 1
            if cube[0][5] != "W":
                move_R1()
                y += 1
            else:
                while cube[0][5] == "W":
                    move_U1()
                    y += 1
                move_R1()
                y += 1
        if cube[4][7] == "W":
            move_F2()
            y += 1
            if cube[0][5] != "W":
                move_R1()
                y += 1
            else:
                while cube[0][5] == "W":
                    move_U1()
                    y += 1
                move_R1()
                y += 1
        # case2 the eges are in the RED face
        if cube[1][3] == "W":
            if cube[0][7] != "W":
                move_F2()
                y += 1
            else:
                while cube[0][7] == "W":
                    move_U1()
                    y += 1
                move_F2()
                y += 1
        if cube[1][5] == "W":
            if cube[0][2] != "W":
                move_B1()
                y += 1
            else:
                while cube[0][2] == "W":
                    move_U1()
                    y += 1
                move_B1()
                y += 1

        if cube[1][1] == "W":
            move_R1()
            y += 1
            if cube[0][2] != "W":
                move_B1()
                y += 1
            else:
                while cube[0][2] == "W":
                    move_U1()
                    y += 1
                move_B1()
                y += 1

        if cube[1][7] == "W":
            move_R2()
            y += 1
            if cube[0][2] != "W":
                move_B1()
                y += 1
            else:
                while cube[0][2] == "W":
                    move_U1()
                    y += 1
                move_B1()
                y += 1
            # case3 the eges are in the ORANGE face
        if cube[3][3] == "W":
            if cube[0][1] != "W":
                move_B2()
                y += 1
            else:
                while cube[0][1] == "W":
                    move_U1()
                    y += 1
                move_B2()
                y += 1
        if cube[3][5] == "W":
            if cube[0][7] != "W":
                move_F1()
                y += 1
            else:
                while cube[0][7] == "W":
                    move_U1()
                    y += 1
                move_F1()
                y += 1

        if cube[3][1] == "W":
            move_L1()
            y += 1
            if cube[0][7] != "W":
                move_F1()
                y += 1
            else:
                while cube[0][7] == "W":
                    move_U1()
                    y += 1
                move_F1()
                y += 1

        if cube[3][7] == "W":
            move_L2()
            y += 1
            if cube[0][7] != "W":
                move_F1()
                y += 1
            else:
                while cube[0][7] == "W":
                    move_U1()
                    y += 1
                move_F1()
                y += 1
            # case4 the eges are in the BLUE face
        if cube[2][3] == "W":
            if cube[0][5] != "W":
                move_R2()
                y += 1
            else:
                while cube[0][5] == "W":
                    move_U1()
                    y += 1
                move_R2()
                y += 1
        if cube[2][5] == "W":
            if cube[0][3] != "W":
                move_L1()
                y += 1
            else:
                while cube[0][3] == "W":
                    move_U1()
                    y += 1
                move_L1()
                y += 1
        if cube[2][1] == "W":
            move_B1()
            y += 1
            if cube[0][3] != "W":
                move_L1()
                y += 1
            else:
                while cube[0][3] == "W":
                    move_U1()
                    y += 1
                move_L1()
                y += 1

        if cube[2][7] == "W":
            move_B2()
            y += 1
            if cube[0][3] != "W":
                move_L1()
                y += 1
            else:
                while cube[0][3] == "W":
                    move_U1()
                    y += 1
                move_L1()
                y += 1

            # case5 the eges are in the YELLOW face
        if cube[5][3] == "W":
            if cube[0][3] != "W":
                move_L2()
                y += 1
                move_L2()
                y += 1
            else:
                while cube[0][3] == "W":
                    move_U1()
                    y += 1
                move_L2()
                y += 1
                move_L2()
                y += 1
        if cube[5][5] == "W":
            if cube[0][5] != "W":
                move_R1()
                y += 1
                move_R1()
                y += 1
            else:
                while cube[0][5] == "W":
                    move_U1()
                    y += 1
                move_R1()
                y += 1
                move_R1()
                y += 1
        if cube[5][1] == "W":
            if cube[0][7] != "W":
                move_F1()
                y += 1
                move_F1()
                y += 1
            else:
                while cube[0][7] == "W":
                    move_U1()
                    y += 1
                move_F1()
                y += 1
                move_F1()
                y += 1
        if cube[5][7] == "W":
            if cube[0][1] != "W":
                move_B2()
                move_B2()
            else:
                while cube[0][1] == "W":
                    move_U1()
                move_B2()
                move_B2()
        x+=1
    #perfect cross

        for x in range(1,5):
            if cube[x][1] != cube[x][4]:
                list_of_movement1[x]()
                list_of_movement1[x]()
        while cube[5][1] == "W" or cube[5][3] == "W" or cube[5][5] == "W" or cube[5][7] == "W":
            for y in range(1, 5):
                fois= 0
                while cube[y][7] != cube[y][4] :
                    fois+=1
                    if fois == 4:
                        break
                    move_D1()
                if cube[y][7] == cube[y][4]:
                    list_of_movement1[y]()
                    list_of_movement1[y]()
    return cube
def perfect_white_face():
    #this is were i defined a way to represent the previous face and the next face depending on where you look at on the cube
    def case_w():
        if cube[0][0]=="W":
            if cube[3][4] or cube[2][2] != cube[2][4]:
                move_L2()
                move_D2()
                move_L1()

        if cube[0][2] == "W" :
            if cube[1][2] != cube[1][4] or cube[2][0] != cube[2][4]:
                move_B2()
                move_D2()
                move_B1()
        if cube[0][6] == "W" :
            if cube[4][0] != cube[4][4] or cube[3][2] != cube[3][4]:
                move_F2()
                move_D2()
                move_F1()
        if cube[0][8] == "W":
            if cube[4][2] != cube[4][2] or cube[1][0] != cube[1][4]:
                move_R2()
                move_D2()
                move_R1()
        print("caseW")
    for y in range(1,5):
        z = y + 1
        x = y - 1
        if y == 1:
            x = 4
        if y == 4:
            z = 1
        if cube[x]:
            pass




move_L1()

move_U1()

move_R1()

move_U2()

move_R2()

move_B2()
move_F1()
move_D2()
move_R2()
move_F2()
move_B2()
move_B2()
move_B1()
move_L2()
move_U1()
move_F1()
move_D2()
move_D1()
move_B1()
move_L2()
move_L1()
move_R2()
move_L2()
move_L1()
move_D2()
move_B2()
move_D1()
move_U1()
move_R1()
move_L1()
move_L2()
move_L2()
move_D1()
move_U2()
move_L2()
move_B1()
move_D2()
move_F2()
move_R1()
move_U2()
move_F1()
move_R1()
move_U1()
move_D2()
move_F2()
move_D1()
move_D1()
move_B1()
move_U2()
move_L2()
move_D2()
move_U1()
move_B1()
move_D2()
move_R2()
move_F1()
move_D1()
move_R2()
move_F2()
move_R1()
move_L2()
move_L1()
move_L2()
move_D1()
move_U1()
move_U2()
move_B1()
move_B1()
move_U2()
move_R2()
move_U2()
move_D2()
move_F2()
move_U1()
move_U1()
move_B1()
move_R1()
move_R2()
move_L2()
move_U1()
move_R2()
move_U2()
move_B2()
move_F2()
move_F1()
move_R1()
move_D2()
move_B1()
move_F1()
move_L2()
move_R2()
move_B1()
move_U2()
move_R2()




white_cross()
perfect_white_face()
print_cube(cube)
