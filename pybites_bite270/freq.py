def freq_digit(num: int) -> int:
        
    digit = [0] * 10
    num_str = str(num)
    curr_max = 0
    
    for n in num_str:
        if n.isdigit():
            freq = int(n)
            digit[freq] +=1
            
            if digit[freq] > curr_max:
                curr_max = digit[freq]
                most_freq = digit.index(max(digit))
    
    return most_freq