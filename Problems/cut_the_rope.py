# Problem Statement:
# You are given a rope of length 5m. Cut the rope into 9 parts such that each part is of equal length.
# Note:Array elements are the points where cut is to be made and round upto 2 decimal place.
# Print the array element.

import numpy as np

rope_length = 5
num_parts = 9

cut_points = np.linspace(0, rope_length, num_parts+1)[1:-1].round(2)
print(cut_points)
for cut_point in cut_points:
    print(cut_point)
