# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

# init vars spain
spain_total_area = 505307
spain_religion = 'Roman Catholic'
spain_language = 'Castilian Spanish'
spain_capital = 'Madrid'
spain_capital_len = len(spain_capital)
spain_gpd = 1.95
spain_population_growth = 0.13
spain_population_count = 47163418

# init vars switzerland
switzerland_total_area = 41277
switzerland_religion = 'Roman Catholic'
switzerland_language = 'German'
switzerland_capital = 'Bern'
switzerland_capital_len = len(switzerland_capital)
switzerland_gpd = 1.11
switzerland_population_growth = 0.65
switzerland_population_count = 8118367

# the exercise
# print(spain_total_area > switzerland_total_area)
print(spain_language == switzerland_language)
print(spain_religion == switzerland_religion)
print(spain_capital_len != switzerland_capital_len)
print(switzerland_gpd > spain_gpd)
print(switzerland_population_growth < 1 and spain_population_growth < 1)
print(spain_population_count > 10000000 or switzerland_population_count > 10000000)
print(spain_population_count > 10000000 or switzerland_population_count > 10000000)