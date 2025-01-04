from collections import Counter
import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()
    print(data)

# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    

    car_year = [car['automaker'] for car in data if car['year'] == year]
    automaker_counts = Counter(car_year)
    
    if automaker_counts:
        return automaker_counts.most_common(1)[0][0]
    return None


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    
    car_models =  [car['model'] for car in data if car['automaker'] == automaker and car['year']==year]

    cars_no_dupes = set(car_models)
    return  cars_no_dupes
    
    


