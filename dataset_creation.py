import json
import random
from enum import Enum, unique

@unique
class NumbersTypes(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    BOTH = 3

dataset = []
dataset_length = 10000
min_no_of_numbers = 5
max_no_of_numbers = 10
min_number = -1000
max_number = 1000

for numbers_type in NumbersTypes:
    is_asc = True
    
    for i in range(dataset_length):
        no_of_numbers = random.choice(range(min_no_of_numbers, max_no_of_numbers))

        if numbers_type == NumbersTypes.POSITIVE:
            numbers = random.sample(range(0, max_number), no_of_numbers)
        elif numbers_type == NumbersTypes.NEGATIVE:
            numbers = random.sample(range(min_number, 0), no_of_numbers)
        else:
            numbers = random.sample(range(min_number, max_number), no_of_numbers)
        
        random.shuffle(numbers)
        sorted_numbers = sorted(numbers) if is_asc else sorted(numbers, reverse=True)
        
        numbers_string = ', '.join(str(x) for x in numbers)
        sorted_numbers_string = ', '.join(str(x) for x in sorted_numbers)
        asc_desc = 'ascending' if is_asc else 'descending'
        sample = 'The sorted {0} order of {1} is {2}'.format(asc_desc, numbers_string, sorted_numbers_string)
        
        dataset.append(sample)
        is_asc = not is_asc

random.shuffle(dataset)
  
with open('dataset.json', 'w+') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)