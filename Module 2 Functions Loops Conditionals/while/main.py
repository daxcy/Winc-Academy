from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

def unique_koala_facts(amount):
    unique_list = []
    i = 0
    limit = 0
    while i < amount:
        fact = random_koala_fact()
        if fact not in unique_list:
            unique_list.append(fact)
            i += 1
        limit += 1
        if limit >= 1000:
            break
    return unique_list

def num_joey_facts():
    unique_list = []
    count = 0
    number_of_joeys = 0
    first_fact = ''
    while True:
        fact = random_koala_fact()
        if first_fact == '':
            first_fact = fact
        if fact not in unique_list:
            unique_list.append(fact)
            if 'joey' in fact:
                number_of_joeys += 1
        if fact == first_fact:
            count += 1
        if count == 10:
            break
    print(number_of_joeys)
    return int(number_of_joeys)

def koala_weight():
    unique_list = []
    while True:
        fact = random_koala_fact()
        if fact not in unique_list:
            unique_list.append(fact)
            if 'kg' in fact:
                start_of_weight = fact.find('kg')-2
                weight = fact[start_of_weight:start_of_weight+2]
                break
    print(weight)
    return int(weight)

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(num_joey_facts())