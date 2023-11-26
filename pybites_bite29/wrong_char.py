def get_index_different_char(chars):
    chars = list(map(str,chars))
    idx_fix = -1
    
    alpf_indx = chars[0].isalnum()
    char_str = str(chars)
    
    alphanum = 0
    for n in chars:
        if str(n).isalnum():
            alphanum += 1
            
    alphanum_main = alphanum > len(chars) / 2
 
    
    for count, char in enumerate(chars):
        alphanum_str = str(char).isalnum()
        if alphanum_main != alphanum_str:
            return count
            