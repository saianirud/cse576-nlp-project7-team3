import json
import random
from enum import Enum, unique

@unique
class NumbersTypes(Enum):
    '''
        Enum for three types of numbers list containing - 1) Only Positive 2) Only Negative 3) Both Positive and Negative
    '''
    POSITIVE = 1
    NEGATIVE = 2
    BOTH = 3


dataset = []

# length of dataset
dataset_length = 100000

# minimum and maximum length of list
min_no_of_numbers = 5
max_no_of_numbers = 10

# range of numbers in the list
min_number = 0
max_number = 100

# alter this list accordingly for different types
numbers_types = [NumbersTypes.POSITIVE, NumbersTypes.NEGATIVE, NumbersTypes.BOTH]

# get the range of each numbers type
numbers_types_range = []
for numbers_type in numbers_types:
    if numbers_type == NumbersTypes.POSITIVE and max_number > 0:
        numbers_types_range.append([0, max_number])
    elif numbers_type == NumbersTypes.NEGATIVE and min_number < 0:
        numbers_types_range.append([min_number, 0])
    elif numbers_type == NumbersTypes.BOTH:
        numbers_types_range.append([min_number, max_number])


for each_range in numbers_types_range:
    # for ascending or descending order
    is_asc = True
    
    for i in range(dataset_length//len(numbers_types_range)):
        # get a random length of list between minimum and maximum
        no_of_numbers = random.choice(range(min_no_of_numbers, max_no_of_numbers))

        # generate numbers list according to its range
        numbers = random.sample(range(each_range[0], each_range[1]), no_of_numbers)
        
        random.shuffle(numbers)
        # get the sorted order
        sorted_numbers = sorted(numbers) if is_asc else sorted(numbers, reverse=True)
        
        # form the input string in the following format
        numbers_string = ', '.join(str(x) for x in numbers)
        sorted_numbers_string = ', '.join(str(x) for x in sorted_numbers)
        asc_desc = 'ascending' if is_asc else 'descending'
        sample = 'The sorted {0} order of {1} is {2}'.format(asc_desc, numbers_string, sorted_numbers_string)
        
        dataset.append({
            'input': numbers,
            'output': sorted_numbers,
            'sample': sample,
            'asc': is_asc
        })
        is_asc = not is_asc

random.shuffle(dataset)
  
# write the generated dataset to a file
with open('dataset_OOD.json', 'w+') as f:
    json.dump(dataset, f, indent=4)