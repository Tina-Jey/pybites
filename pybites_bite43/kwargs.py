def get_profile(**kwargs):
    
    name = 'julian'
    profession = 'programmer'
   
    
    for n, p in kwargs.items():
        
        if n not in ['name', 'profession']:
            raise TypeError
        
        elif n  == 'name':
            name = p
        
        elif n == 'profession':
            profession = p
            

    return f'{name} is a {profession}'

results = get_profile()
print(results)