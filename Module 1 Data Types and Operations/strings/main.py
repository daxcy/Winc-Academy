# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_name_0 = 'Ruud Gullit'
scorer_name_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = f'{scorer_name_0} {goal_0}, {scorer_name_1} {goal_1}'
print(scorers)

report = f'{scorer_name_0} scored in the {goal_0}nd minute\n{scorer_name_1} scored in the {goal_1}th minute'
print(report)

player = 'Berry van Aerle'

# Set first name
end_of_first_name = player.find(' ')
first_name = player[:end_of_first_name]
print(first_name)

# Set last name
last_name= player[end_of_first_name + 1:] # Reusing end_of_first_name as we know where the space ends and adding +1 for the start of the last name
last_name_len = len(last_name)
print(last_name)
print(last_name_len)

# Create short name
name_short = first_name[0] + '. ' + last_name
print(name_short)

# Create chant without a space at the end
chant = (first_name + '! ' ) * len(first_name)
chant = chant[:-1]
print(chant)

# Double check if space 
good_chant = (chant[-1] != ' ')
print(good_chant)