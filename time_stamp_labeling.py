import math
from Arm import Arm3Link
from itertools import permutations
import numpy as np
import datetime

if __name__ == '__main__':
    # recorded time --------------------- modify as needed
    begin_time = 70412 
    duration_between = 10
    arm = Arm3Link()

    #coordinates of the buttons (base_rotation, x, y)
    coordinates = [1,2,3,4]

    p = permutations(coordinates,len(coordinates))

    #entire test suite
    running_set = []

    # #iterate through permutations
    # with open ('timestamps/alexa_p.txt', 'w') as f:
    #     c_counter = 0
    #     for permutation in p:
    #         #all joint rotation degrees for a single permutation
    #         for i in permutation:
    #             if c_counter ==0:
    #                 f.write(str(i)+' at UTC TIME'+str(datetime.timedelta(seconds=begin_time))+ "\n")
    #                 c_counter = 1
    #             else:
    #                 f.write(str(i)+' at UTC TIME '+str(datetime.timedelta(seconds=begin_time+duration_between))+ "\n")
    #                 begin_time=begin_time+duration_between


    # timestamp labeling for repeating button presses.
    with open ('timestamps/alexa_b.txt', 'w') as f:
         c_counter = 0
         for i in coordinates:
             for j in range(15):
                if c_counter ==0:
                    f.write(str(i)+' at UTC TIME'+str(datetime.timedelta(seconds=begin_time))+ "\n")
                    c_counter = 1
                else:
                    f.write(str(i)+' at UTC TIME '+str(datetime.timedelta(seconds=begin_time+duration_between))+ "\n")
                    begin_time=begin_time+duration_between