import numpy as np

def rescale(input_array):
    "rescale and array from 0 to 1."
    low = np.min(input_array)
    high = np.max(input_array)
    return ((input_array - low) / (high - low))*100


