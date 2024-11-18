"""import the tools that I need """
from move import *

"""zone to scramble the cube with some moves"""
move_D2()

"""useful variables"""
start = cube
pruned = []
open_state = []
pre_open = []
current = []
path = []
iteration = 0
move_set1 = [move_U1, move_R1, move_B1, move_L1, move_F1, move_B1, move_UU, move_DD, move_LL, move_RR, move_FF, move_BB]
move_set1_undo = [move_U2, move_R2, move_B2, move_L2, move_F2, move_B2,
                    move_UU, move_DD, move_LL, move_RR, move_FF, move_BB]
move_set2 = [move_U2, move_R2, move_B2, move_L2, move_F2, move_B2]
move_set2_undo =[move_U1, move_R1, move_B1, move_L1, move_F1, move_B1]
continue_algo = True
continue_iteration = True

"""functions"""
# calculate the heuristic for the current state of cube
def heuristic(current, goal):
    dif = 0
    for face_index in range(len(current)):
        for square_index in range(len(current[face_index])):
            if current[face_index][square_index] != goal[face_index][square_index]:
                dif += 1
    return dif / 20

# calculate the g_score for the current state of the cube
def g(start, current):
    dif = 0
    r = 0
    for y in range(len(current)):
        for x in current[0]:
            if x != start[0][r]:
                dif += 1
    return dif / 20

# calculate the f_score and classify them  for every possible child of the current cube
def get_f_scores(threshold):
    pre_open.clear()
    for x in range(len(move_set1)):
        move_set1[x]()
        f = heuristic(cube, save) + g(start, cube)
        if f <= threshold:
            pre_open.append([move_set1[x], f, heuristic(cube, save), cube])
        if f > threshold:
            pruned.append([move_set1[x], f, heuristic(cube, save), cube])
        move_set1_undo[x]()

    for x in range(len(move_set2)):
        move_set2[x]()
        f = heuristic(cube, save) + g(start, cube)
        if f <= threshold:
            pre_open.append([move_set1[x], f, heuristic(cube, save), cube])
        if f > threshold:
            pruned.append([move_set1[x], f, heuristic(cube, save), cube])
        move_set2_undo[x]()
    pre_open.sort(key=lambda x: (x[1], x[2]))

"""algorythm"""
threshold= heuristic(cube, save) + g(start, cube)
while continue_algo:
    iteration += 1
    print(iteration)

    continue_iteration=True
    # we handle the case for the first iteration
    if iteration == 1:
        get_f_scores(threshold)
        continue

    # we handle the case for the other iterations
    elif iteration > 1:
        while continue_iteration:
            print("a")
            # we set the new threshold as the least value in the p_runned if there is something in the prunned list
            if pruned:
                lowest_node = min(pruned, key=lambda x: (x[1], x[2]))
                threshold = lowest_node[1]
            # we can now clear the prunned  list before starting the new iteration
            pruned.clear()
            # we also clear the open list before starting a new iteration
            open_state.clear()
            # we try to see if there is something in the open_state  list and if not we start at the starting node
            if not open_state:
                cube= start
                # we clear the pre_open list before getting the f_scores of the possible children
                pre_open.clear()
                get_f_scores(threshold)

                # we had the element in the open list as the prior elements
                open_state= pre_open + open_state
            # now that we have something in the open list we can handle the case where there is something inside it
            elif open_state:
                # we use the for loop to check and evaluate the child of every node in the list open_state
                for node_to_explore in open_state:
                    # we clean the pre_open list every time that we check for a new element in the open list
                    pre_open.clear()
                    # we set the cube to the first node to visit in the open states list
                    cube= open_state[0][3]
                    # now  that we are exploring that node to avoid repetition we delete that node from the open list
                    open_state.pop(0)
                    # we check if the cube is solved
                    if cube == save:
                        continue_algo = False
                        continue_iteration = False
                    # we calculate the f score for each child of the current state and we add them to the open list
                    get_f_scores(threshold)
                    open_state = pre_open + open_state
                    # we check if there is something in the open_state. if not we got to  the next iteration
                    if not open_state:
                        continue_iteration = False
print("si tu vois cela cest que sa marche!!!!!")