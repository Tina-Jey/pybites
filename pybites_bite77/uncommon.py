from operator import length_hint

def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    
    new = set(my_cities) - set(other_cities)
    new2 = set(other_cities) - set(my_cities)

    new_list = list(new)
    new_list2 = list(new2)

    res = new_list + new_list2

    return length_hint(res)


my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']
print(uncommon_cities(my_cities, other_cities))