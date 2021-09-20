# Automated_IoT_Traffic_Generation
This repo contains essential codes needed for using the braccio robotic arm to perform automate IoT device interactions.

# System Requirements
Python versions of 2.7.18 or python3 3.8.5 or above are supported

# Installation instructions
modules to install: numpy, scipy, math, pandas, matplotlib, seaborn, sklearn,itertools.

Clone the repo into your local device using:
```
git clone https://github.com/Chasexj/Automated_IoT_Traffic_Generation.git
```


# generation.py
script to 

(1) produce corresponding arm rotations given x and y coordinates

Note: scripts uses the Arm.py module which is an open source script for inverse kinematics from https://github.com/Chasexj/robotic_surgery/tree/master/src/ros/modified_arm/InvKin.

(2) produce the permutation based test sets.
 
# braccio_code.py
script to produce permutation/repetition based test suites (in language Arduino Software (IDE) readable language) given the button-corresponding rotations.

# time_stamp_labeling.py
script to generate txt files containing relative timestamps of the button presses.

# data_label.py
labeling nprint encoded pcaps packets with corresponding button presses according to the timestamps.

# rfc.py
random forest classifier to perform machine learning evaluation on the labeled data.

# nprint
note that nprint is used to encode the captured pcaps, specific usage of nprint can be found at https://nprint.github.io/nprint/
