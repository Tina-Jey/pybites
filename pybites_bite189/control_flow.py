IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    
    filtered_list = []
    count = 0
    
    for name in names:
        if count >= MAX_NAMES:
            break
        
        if name[0] == IGNORE_CHAR:
            continue
        elif any(d.isdigit() for d in name):
        #name.isdigit():
            continue
        elif name[0] == QUIT_CHAR:
            break
        else:
            filtered_list.append(name)
            count += 1

            
    return filtered_list   