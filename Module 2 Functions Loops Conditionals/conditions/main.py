# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, time_of_day, milk_cows, cow_location, season, slurry_tank, grass_status):
    action = 'wait'

    if cow_location == 'pasture':
        if weather == 'rainy' or time_of_day == 'night':
            action = 'take cows to cowshed'
        elif  milk_cows == True:
            action = 'milk cows'
        elif slurry_tank == True and (weather != 'sunny' or weather != "windy"):
            action = 'fertilize pasture'
        elif grass_status == True and season == 'spring' and weather == 'sunny':
            action = 'mow grass'

        if action != 'wait':
            action = 'take cows to cowshed\n' + action + '\ntake cows back to pasture'
            print(action)
            return action

    if cow_location == 'pasture' and (weather == 'rainy' or time_of_day == 'night'):
        action = 'take cows to cowshed'
    elif  milk_cows == True and cow_location == 'cowshed':
        action = 'milk cows'
    elif slurry_tank == True and cow_location == 'cowshed' and (weather != 'sunny' or weather != "windy"):
        action = 'fertilize pasture'
    elif grass_status == True and season == 'spring' and weather == 'sunny' and cow_location == 'cowshed':
        action = 'mow grass'
    print(action)
    return action

farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)
farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
farm_action('windy', 'night', True, 'cowshed', 'winter', True, True)
farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)