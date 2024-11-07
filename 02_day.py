import json

lines = []

with open("input_day2.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

# print(lines[:5])

games_dict = {}

for line in lines:
    line_split = line.split(":")
    # print(line_split)
    game_key = line_split[0]
    game_values = line_split[1].strip()
    games_dict[game_key] = game_values

# formatted_dict = json.dumps(games_dict, indent=4)
# print(formatted_dict)

for game, values in games_dict.items():
    sets_list = values.split(";")
    sets_list = [set.strip() for set in sets_list]
    # print(sets_list)
    games_dict[game] = sets_list

# formatted_dict = json.dumps(games_dict, indent=4)
# print(formatted_dict)

# which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

for game, values in games_dict.items():
    sets_list = []
    for set in values:
        set_split = set.split(", ")
        sets_list.append(set_split)
    games_dict[game] = sets_list

# formatted_dict = json.dumps(games_dict, indent=4)
# print(formatted_dict)

for game, values in games_dict.items():
    new_sets_list = []
    for set in values:
        cubes_count = {}
        for cubes in set:
            cubes_split = cubes.split(" ")
            color = cubes_split[1]
            count = int(cubes_split[0])
            cubes_count[color] = count
        new_sets_list.append(cubes_count)
    games_dict[game] = new_sets_list

# formatted_dict = json.dumps(games_dict, indent=4)
# print(formatted_dict)

games_possible = []
games_impossible = []


for game, values in games_dict.items():
    possible = True
    for set in values:
        red = set.get("red", 0)
        green = set.get("green", 0)
        blue = set.get("blue", 0)
        if red > 12 or green > 13 or blue > 14:
            possible = False
    if possible:
        games_possible.append(game)
    else:
        games_impossible.append(game)


games_possible_ids = []
for game in games_possible:
    game_split = game.split(" ")
    game_nbr = game_split[1]
    games_possible_ids.append(int(game_nbr))

sum_of_IDs = sum(games_possible_ids)

print(sum_of_IDs)


# For each game, find the minimum set of cubes that must have been present.
# What is the sum of the power of these sets?

min_set = []

for game, values in games_dict.items():
    red = -1
    green = -1
    blue = -1
    for set in values:
        red_value = set.get("red", 0)
        green_value = set.get("green", 0)
        blue_value = set.get("blue", 0)
        if red_value > red:
            red = red_value
        if green_value > green:
            green = green_value
        if blue_value > blue:
            blue = blue_value
    min_set.append([red, blue, green])

# print(min_set)

games_power = []

for game in min_set:
    power = 1
    for number in game:
        power *= number
    games_power.append(power)

# print(games_power)

sum_of_powers = sum(games_power)

print(sum_of_powers)
