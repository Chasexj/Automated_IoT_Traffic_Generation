import math
from Arm import Arm3Link
from itertools import permutations
import numpy as np

if __name__ == '__main__':
    #creat the Arm3Link class for inverse kinematics
    arm = Arm3Link()

    #coordinates of the buttons (base_rotation, x, y)
    coordinates = [(30,12,13),(20,15,14),
                    (90,18,16),(3,20,15),
                    (28,13,19)]

    #specifying the amount of errors in each joint
    ############# plot the errors
    ############# curve fit
    ############# video a demo
    ############# Data Collection - IoT Inspector
    ############# Or Rasp P

    joint_errors = (2,3,1)
    coordinates_dic = {}

    #compute the buttons' corresponding joint rotations
    for button in coordinates:
        
        #base_rotation is pre-specified
        base_rotation = button[0]
        xy = []
        xy.append(button[1])
        xy.append(button[2])

        #joint rotation (raw with no error input) in radian
        joint_rotations = arm.inv_kin(xy=xy)

        #radian -> degree with error input
        for i in range(3):
            joint_rotations[i] = math.degrees(joint_rotations[i]) + joint_errors[i]
        joint_rotations = np.insert(joint_rotations,0,base_rotation)

        #dictionary with corrected rotations as values to button keys
        coordinates_dic[button] = joint_rotations

    #method of arranging the buttons (combination, permutation, etc)
    p = permutations(coordinates,len(coordinates))

    #entire test suite
    running_set = []

    #iterate through permutations
    for permutation in p:

        #all joint rotation degrees for a single permutation
        all_rotations = []
        for button in permutation:
            all_rotations.append(coordinates_dic[button])

        #append to all permutation joint rotations
        running_set.append(all_rotations)
    
    #print result, or output to file
    permutation_counter = 0
    with open ('ouput.txt', 'w') as f:
        for permutation in running_set:

            # permutation number
            f.write('Permutation Number '+ str(permutation_counter)+'\n')
            permutation_counter = permutation_counter+1
            for button_rotations in permutation:
                end_comma = 0
                for joint_rotation in button_rotations:
                    if end_comma != 3:
                        f.write(str(joint_rotation)+' ,')
                        end_comma = end_comma+1
                    else:
                        f.write(str(joint_rotation)+'\n')

            #f.write('Returning to default setting'+'\n') # USE WHEN RETURN TO DEFAULT BETWEEN PERMUTATIONS
            #f.write('0 ,90 ,90 ,90'+'\n') # USE WHEN RETURN TO DEFAULT BETWEEN 
            
    #can modify the output syntax (add non moving joint rotations) before writing to file