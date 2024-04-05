import numpy as np 

def solution(n):
    sqrt_result = np.sqrt(n)
    if float(sqrt_result).is_integer():
        return (sqrt_result+1)**2
    else:
        return -1 
    