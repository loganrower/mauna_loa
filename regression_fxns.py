##Contains Python functions for HW08, BDS 311
##These functions will be generated collaboratively and called in each user's separate Jupyter notebook

#import standard packages here

import numpy as np


def make_standard_units(input_array):
    '''Converts input_array to standard_units, where data has mean 0 and standard deviation of 1
        INPUT: data array
        OUTPUT: array in standard units'''
    mean_subtracted_array = input_array - np.mean(input_array)
    normalized_array = mean_subtracted_array/np.std(input_array)
    return normalized_array

    
def calc_corrcoef_from_standardized_input(array1,array2):
    '''Calculates Pearson correlation coefficient from two arrays in standard units
    INPUT: array1, array2: In standard units
    OUTPUT: Pearson correlation coefficient'''
    # the two arrays will first be converted into standard units using make_standard_units
    array_1_su = make_standard_units(array1)
    array_2_su = make_standard_units(array2)
    corrcoef = np.mean(array_1_su*array_2_su)
    return corrcoef

def get_regression_parameters(array1, array2):
    '''Calculates regression parameters from two input arrays
    INPUT: array1, array2: two data arrays
    OUTPUT: regression_array, length 2: regression_array[0] is slope and regression_array[1] is intercept'''

    regression_array = np.empty(2)
    slope = calc_corrcoef_from_standardized_input(array1, array2)*(np.std(array2)/np.std(array1))
    intercept = np.mean(array2) - (slope * np.mean(array1))
    regression_array[0] = slope
    regression_array[1] = intercept
    return regression_array
'''
Remember that the slope of the regression line is `correlation_coefficient * (sd(y)/sd(x))`.
The intercept can be calculated from the equation of a line using the mean of the data and the slopes `meany = slope * meanx + intercept`
'''
