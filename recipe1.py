
from pprint import pprint

cook_book = {}
with open('Recipe.txt', 'rt') as file:
    #cook_book = {}
    for line in file:
        recep_name = line.strip()
        ingredients_count = file.readline()
        food = []
        for p in range(int(ingredients_count)):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            food.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[recep_name] = food

# pprint(cook_book)
pprint(f'cook_book = {cook_book}')


cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'}, {'ingredient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'}, {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}],
             'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': '1', 'measure': 'шт'}, {'ingredient_name': 'Вода', 'quantity': '2', 'measure': 'л'}, {'ingredient_name': 'Мед', 'quantity': '3', 'measure': 'ст.л'}, {'ingredient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}],
             'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'}, {'ingredient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч'}, {'ingredient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}],
             'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': '500', 'measure': 'г'}, {'ingredient_name': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'}, {'ingredient_name': 'Лаваш', 'quantity': '2', 'measure': 'шт'}, {'ingredient_name': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'}, {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}]}

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])


# pprint(f'cook_book = {cook_book}')
#
# print(cook_book)


# cook_book = {}
# with open('Recipe.txt', 'rt') as file:
#     for line in file:
#         #print(line)
#         recep_name = line.strip().split('\n\n')
#         #print(recep_name)
#         food = []
#         count = file.readline()
#         for i in range(int(count)):
#             dish_ing = file.readline()
#             ingredient_name, quantity, measure = dish_ing.strip().split(' | ')
#             food.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
#             dep = {recep_name: food}
#             file.readline()
#         separate = file.readline()
#         cook_book.update(dep)
#         cook_book[recep_name] = food
# print(f'cook_book = {cook_book}')
#print(cook_book)

# # cook_book = {'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': '2', 'measure': 'шт'}, {'ingredient_name': 'Молоко', 'quantity': '100', 'measure': 'мл'}, {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}],
#              'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': '1', 'measure': 'шт'}, {'ingredient_name': 'Вода', 'quantity': '2', 'measure': 'л'}, {'ingredient_name': 'Мед', 'quantity': '3', 'measure': 'ст.л'}, {'ingredient_name': 'Соевый соус', 'quantity': '60', 'measure': 'мл'}],
#              'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'}, {'ingredient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч'}, {'ingredient_name': 'Сыр гауда', 'quantity': '100', 'measure': 'г'}],
#              'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': '500', 'measure': 'г'}, {'ingredient_name': 'Перец сладкий', 'quantity': '1', 'measure': 'шт'}, {'ingredient_name': 'Лаваш', 'quantity': '2', 'measure': 'шт'}, {'ingredient_name': 'Винный уксус', 'quantity': '1', 'measure': 'ст.л'}, {'ingredient_name': 'Помидор', 'quantity': '2', 'measure': 'шт'}]}
# #
# def get_shop_list_by_dishes(cook_book):
#     cook = {}
#     for dishes, person_count in zip(cook_book)
#         cook
#
#
#
#
# def get_shop_list_by_dishes(dishes, person_count):
#     cook = {}
#     for dish in dishes:
#         if dish in cook_book:
#
#             for ingredient_name in cook_book[dish]:
#                 if dish in cook:
#
#                     ingredient_name.append(cook)
#                 else:
#                     ingredient_name.apped(int(cook_book['quantity']) * int(person_count))
#
#                 if dish in cook.keys():
#                     print(cook[ingredient_name])
#                 else:
#                     print(cook[int(cook_book['quantity']) * int(person_count)])
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#
#
# #
# #
#
# def list_of_stores_with_ingredients(dishes, person_count):
#      total = {}
#      for dish in dishes:
#          if dish in cook_book:
#            for exist in cook_book[dish]:
#
#              total = {'measure': cook_book['measure'],'quantity': (int(cook_book['quantity'])*int(person_count))}
#          else:
#              print(f'Блюда "{dish}" нет в книге рецептов')
#      return total

 # list_of_stores_with_ingredients(["Омлет"], 2)

# print(dish)

# def get_shop_list_by_dishes(dishes, person_count):
#     new_cook = {}
#     cook_book = my_cook_book()
#     for dish in dishes:
#         if dish in cook_book:
#             for ingredient in cook_book[dish]:
#                 ingredient['quantity'] *= person_count
#                 new_cook.setdefault(ingredient['ingredient_name'], ingredient)
#                 print(new_cook)
# #


# def get_shop_list_by_dishes(person_count: int, dishes: list):
#     result = {}
#     for dish in dishes:
#         if dish in cook_book:
#             for consist in cook_book[dish]:
#                 if consist['ingredient_name'] in result:
#                     result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
#                 else:
#                     result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
#         else:
#             print('Такого блюда нет в книге')
#     print(result)
# get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])

