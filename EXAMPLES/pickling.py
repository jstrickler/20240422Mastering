import pickle
from pprint import pprint

# some data structures
airports = {
    'RDU': 'Raleigh-Durham', 'IAD': 'Dulles', 'MGW': 'Morgantown',
    'EWR': 'Newark', 'LAX': 'Los Angeles', 'ORD': 'Chicago'
}

colors = [
    'red', 'blue', 'green', 'yellow', 'black',
    'white', 'orange', 'brown', 'purple'
]

values = [
    3/7, 1/9, 14.5
]

data = [  # list of data structures
    colors,
    airports,
    values,
]

with open('../TEMP/pickled_data.pic', 'wb') as pic_out:  # open pickle file for writing in binary mode
    pickle.dump(data, pic_out)  # serialize data structures to pickle file
    pic_data = pickle.dumps(data)  # serialize to binary string (bytes)

with open('../TEMP/pickled_data.pic', 'rb') as pic_in:  # open pickle file for reading in binary mode
    pickled_data = pickle.load(pic_in)  # de-serialize pickle file back into data structures
    orig_data = pickle.loads(pic_data)

pprint(pickled_data)  # view data structures
print('-' * 60)
pprint(orig_data)