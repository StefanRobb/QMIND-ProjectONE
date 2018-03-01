# Created by Joey Tepperman on March 1st 2018
# This program adds an ingredients list to recipes.json
import json

data = json.load(open('recipes.json'))
ing_list = {}
for recipe in data['recipes']:
    for ing in recipe['ingredients']:
        if not ing['name'] in ing_list:
            ing_list[ing['name']] = [ing['measurement']]
        else:
            if not ing['measurement'] in ing_list[ing['name']]:
                ing_list[ing['name']].append(ing['measurement'])
final_dict = {'ingredients list':ing_list}
with open('ingredients_list.json', 'w') as fp:
    json.dump(final_dict, fp)