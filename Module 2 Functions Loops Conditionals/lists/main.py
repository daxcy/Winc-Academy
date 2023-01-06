# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

list_of_won_golden_globe = ['jaws', 'memoirs of a geisha', 'toto', 'hydra', 'hoi', 'Fahrenheit', 'Old Is New']
list_of_toto_albums = ['toto', 'toto iv', 'Fahrenheit', 'Old Is New']

def alphabetical_order(list):
    list.sort()
    return list

def won_golden_globe(film_name):
    result = True if film_name.lower() in list_of_won_golden_globe else False
    return result

def remove_toto_albums(film_list):
    clean_list = list(set(film_list) - set(list_of_toto_albums))
    return clean_list

test = won_golden_globe('jaws')
test2 = remove_toto_albums(list_of_won_golden_globe)
print(test)