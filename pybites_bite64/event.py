#import itertools

#names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
#locations = 'DE ES AUS NL BR US - - '.split()
#confirmed = [False, True, True, False, True, '-', '-', '-']


#def get_attendees():
#    for participant in zip(names, locations, confirmed):
#        print(participant)


# better solution:
from itertools import zip_longest

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in zip_longest(names, locations, confirmed, fillvalue='-'):
        print(participant)


if __name__ == '__main__':
    get_attendees()
