import jsonlines
import random
import os

for no_of_digits in [2, 3, 4]:

    # length of dataset
    dataset_length = 100000

    # minimum and maximum length of list
    min_no_of_numbers = 3
    max_no_of_numbers = 11

    # range of numbers in the list
    min_number = 0
    if no_of_digits == 2:
        max_number = 100
        path = 'dataset_pretrain/sort_99'
    elif no_of_digits == 3:
        max_number = 1000
        path = 'dataset_pretrain/sort_999'
    elif no_of_digits == 4:
        max_number = 10000
        path = 'dataset_pretrain/sort_9999'
    

    if not os.path.exists(path):
        os.makedirs(path)

    for file in ['train', 'val', 'test']:

        dataset = []
            
        for i in range(dataset_length):
            # get a random length of list between minimum and maximum
            no_of_numbers = random.choice(range(min_no_of_numbers, max_no_of_numbers))

            # generate numbers list according to its range
            numbers = random.sample(range(min_number, max_number), no_of_numbers)
            
            random.shuffle(numbers)
            
            # get the sorted order
            sorted_numbers = sorted(numbers)
            numbers_string = ' '.join(str(x) for x in numbers)
            sorted_numbers_string = ' '.join(str(x) for x in sorted_numbers)
            asc_text = 'The sorted ascending order of {0} is {1}'.format(numbers_string, sorted_numbers_string)

            rev_sorted_numbers = sorted(numbers, reverse=True)
            numbers_string = ' '.join(str(x) for x in numbers)
            rev_sorted_numbers_string = ' '.join(str(x) for x in rev_sorted_numbers)
            desc_text = 'The sorted descending order of {0} is {1}'.format(numbers_string, rev_sorted_numbers_string)
            
            dataset.append({
                'numbers': numbers,
                'asc_text': asc_text,
                'desc_text': desc_text,
                'numbers_str': numbers_string,
                'asc_ans': sorted_numbers_string,
                'desc_ans': rev_sorted_numbers_string
            })

        random.shuffle(dataset)
        
        # write the generated dataset to a file
        with jsonlines.open(path + '/' + file + '.jsonl', 'w') as writer:
            writer.write_all(dataset)
