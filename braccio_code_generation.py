import math
from Arm import Arm3Link
from itertools import permutations
import numpy as np
import datetime

if __name__ == '__main__':
    #creat the Arm3Link class for inverse kinematics
    begin_time = 4660
    duration_between = 10.4237288136
    arm = Arm3Link()

    #rotations of the buttons (base_rotation, x, y) --------------------- modify as needed
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
    
    permutation_counter = 0
    first_button = True

    # permutation based braccio codes
    with open ('braccio_codes/ouput2.txt', 'w') as f:
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
                        if first_button:
                            f.write(str(joint_rotation)+"); //at UTC TIME "+str(datetime.timedelta(seconds=begin_time))+ "\n")
                            first_button=False
                        else:
                            f.write(str(joint_rotation)+"); //at UTC TIME "+str(datetime.timedelta(seconds=begin_time+duration_between))+ "\n")
                            begin_time=begin_time+duration_between
                        f.write("Braccio.ServoMovement(30,         90, 75, 90, 170,    90,  73); \n")
                        f.write("delay(5000);\n")


    # # repeated pressing of buttons
    # with open ('braccio_codes/ouput.txt', 'w') as f:
    #     f.write("Braccio.ServoMovement(30,         90, 75, 90, 170,    90,  73);\n")
    #     c_counter = 0
    #     for i in coordinates:
    #         f.write('//Button '+ str(i)+'\n')
    #         for j in range(15):
    #             if c_counter ==0:
    #                 f.write("Braccio.ServoMovement("+str(i).strip('()')+'); //at UTC TIME'+str(datetime.timedelta(seconds=begin_time))+ "\n")
    #                 c_counter = 1
    #             else:
    #                 f.write("Braccio.ServoMovement("+str(i).strip('()')+'); //at UTC TIME '+str(datetime.timedelta(seconds=begin_time+duration_between))+ "\n")
    #                 begin_time=begin_time+duration_between
    #             f.write("Braccio.ServoMovement(30,         90, 75, 90, 170,    90,  73); \n")
    #             f.write("delay(5000);\n")