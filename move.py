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
