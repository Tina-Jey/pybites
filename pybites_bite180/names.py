from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)

    d = defaultdict(list)
    
    new_data = data.split('\n')[1:]
    
    for line in new_data:
        if line:
            last_name, first_name, country_code = line.split(',')
        #names = f"{last_name}{first_name}"
            d[country_code].append(f'{first_name} {last_name}')
        
    return d