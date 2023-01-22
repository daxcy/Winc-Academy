from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
list_shortest_names = []
countries_vowels_list = []


def shortest_names(list_of_countries):
    shortest_country = 999 # set value to 999 for start loop
    for country in list_of_countries:
        # create list shortest names
        if len(country) <= shortest_country:
            if len(country) == shortest_country:
                list_shortest_names.append(country)
                # print('country gelijk aan ' + country)
            else:
                list_shortest_names = [country]
                # print('country kleiner ' + country)
                shortest_country = len(country)
    return list_shortest_names

def most_vowels(list_of_countries):
    # create list with countries and counted vowels
    for country in list_of_countries:
        number_of_vowels = 0 # set to 0 before start loop
        for vowel in country:
            if vowel.lower() in ["a", "e", "i", "o", "u"]:
                number_of_vowels += 1
        countries_vowels_list.append([country, number_of_vowels])

    temp_list = sorted(countries_vowels_list, key=lambda x: x[1], reverse=True)
    sorted_countries_list = []
    for i in temp_list[:3]:
        sorted_countries_list.append(i[0])

    return sorted_countries_list

def alphabet_set(list_of_countries):
    letters_needed = [] # set to 0 before start loop
    alphabet_countries = []
    alphabet = ['a','b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for country in list_of_countries:
        for vowel in country:
            if vowel.lower() not in letters_needed and vowel.lower() in alphabet:
                letters_needed.append(vowel.lower())
                if country not in alphabet_countries:
                    alphabet_countries.append(country)

    return alphabet_countries

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    temp = shortest_names(countries)
    print(temp)
    temp = most_vowels(countries)
    print(temp)
    temp = alphabet_set(countries)
    print(temp)


