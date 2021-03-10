import math
from Arm import Arm3Link
from itertools import permutations
import numpy as np

if __name__ == '__main__':
    #creat the Arm3Link class for inverse kinematics
    arm = Arm3Link()

    #coordinates of the buttons (base_rotation, x, y)
    coordinates = [(30,         79, 89, 180, 177,    90,  73),
    (30,         87, 89, 180, 177,    90,  73),
                    (30,         98, 89, 180, 177,    90,  73),
                    (30,         105, 93, 180, 170,    90,  73)]

    p = permutations(coordinates,len(coordinates))

    #entire test suite
    running_set = []

    #iterate through permutations
    for permutation in p:
        #all joint rotation degrees for a single permutation
        all_rotations = []
        for button in permutation:
            all_rotations.append(button)

        #append to all permutation joint rotations
        running_set.append(all_rotations)
    
    #print result, or output to file
    permutation_counter = 0
    with open ('ouput2.txt', 'w') as f:
        f.write("Braccio.ServoMovement(30,         90, 75, 90, 170,    90,  73);\n")
        for permutation in running_set:
            # permutation number
            f.write('//Permutation Number '+ str(permutation_counter)+'\n')
            permutation_counter = permutation_counter+1
            for button_rotations in permutation:
                end_comma = 0
                for joint_rotation in button_rotations:
                    if end_comma == 0:
                        f.write("Braccio.ServoMovement("+str(joint_rotation)+',')
                        end_comma = end_comma+1
                    elif end_comma != 6:
                        f.write(str(joint_rotation)+',')
                        end_comma = end_comma+1
                    else:
                        f.write(str(joint_rotation)+');\n')
                        f.write("delay(200);\n")
                        f.write("Braccio.ServoMovement(30,         90, 75, 90, 170,    90,  73);\n")
                        f.write("delay(200);\n")


            #f.write('Returning to default setting'+'\n') # USE WHEN RETURN TO DEFAULT BETWEEN PERMUTATIONS
            #f.write('0 ,90 ,90 ,90'+'\n') # USE WHEN RETURN TO DEFAULT BETWEEN 
            
    #can modify the output syntax (add non moving joint rotations) before writing to file

    #Braccio.ServoMovement(30,         90, 90, 90, 90, 90,  73); 