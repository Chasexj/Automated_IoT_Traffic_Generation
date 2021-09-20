# Automated_IoT_Traffic_Generation

This repo contains essential codes needed for using the braccio robotic arm to perform automate IoT device interactions.

# generation.py
script to (1) produce corresponding arm rotations given x and y coordinates (using https://github.com/Chasexj/robotic_surgery/tree/master/src/ros/modified_arm/InvKin, an open source script for inverse kinematics), (2) produce the permutation based test sets.
 
# braccio_code.py
script to produce permutation/repetition based test suites (in language Arduino Software (IDE) readable language) given the button-corresponding rotations.

# time_stamp_labeling.py
script to generate txt files containing relative timestamps of the button presses.

# data_label.py
labeling nprint encoded pcaps packets with corresponding button presses according to the timestamps.

# rfc.py
random forest classifier to perform machine learning evaluation on the labeled data.
