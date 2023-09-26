
from collections import deque

def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    
    #rotate_string_1st = str[0: len(string)-n]
    #rotate_string_2nd = str[0: len(string)-n : ]
        
    my_deque = deque(string)
    if n > 0 :
        my_deque.rotate(-n)
    else:
        my_deque.rotate(abs(n))
    return ''.join(my_deque)
    
