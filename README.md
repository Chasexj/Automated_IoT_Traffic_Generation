# Automated_IoT_Traffic_Generation
This repo contains essential code for using the Braccio robotic arm to automate IoT device interactions.

## Citing
We encourage the use of this repository for research. If you publish the results of research using the code contained in this repository, we ask that you cite the following paper:

X. Jiang and N. Apthorpe. "Automating Internet of Things Network Traffic Collection with Robotic Arm Interactions." arXiv preprint arXiv:2110.00060. 2021.

## System Requirements
Python versions of 2.7.18 or python3 3.8.5 or above are supported

## Installation instructions
Modules to install: numpy, scipy, math, pandas, matplotlib, seaborn, sklearn,itertools.

Clone the repo into your local device using:
```
git clone https://github.com/Chasexj/Automated_IoT_Traffic_Generation.git
```

## Repository Overview

### generation.py
Script to 

(1) produce corresponding arm rotations given x and y coordinates (as specified in comment on line 10)

Note: scripts uses the Arm.py module which is an open source script for inverse kinematics from https://github.com/Chasexj/robotic_surgery/tree/master/src/ros/modified_arm/InvKin.

(2) produce the permutation based test sets.
 
### braccio_code_generation.py
Script to produce permutation/repetition based test suites (in language Arduino Software (IDE) readable language) given the button-corresponding rotations (as specified in comment on line 13).

### time_stamp_labeling.py
Script to generate txt files containing relative timestamps of the button presses. (as specified in comment on line 8)

### data_label.py 
Labeling nprint encoded pcaps packets with corresponding button presses according to the timestamps. (as specified in comment on line 8)

### rfc.py
Random forest classifier to perform machine learning evaluation on the labeled data.

### nprint
Note that nprint is used to encode the captured pcaps, specific usage of nprint can be found at https://nprint.github.io/nprint/
