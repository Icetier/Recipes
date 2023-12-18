import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'recipes.txt')

with open(file_path, 'r', encoding='utf-8') as f:

    cook_book: dict[str, list[dict[str, any]]] = {}
    ing_list = {}
    for string in f:
        dish = string.strip()
        ingredients = int(f.readline().strip())
        book = []
        for value in range(ingredients):
            ingredient, quantity, measure = f.readline().strip().split('|')
            book.append({'Ингредиент': ingredient, 'количество': quantity, 'объём в': measure})
        cook_book[dish] = book
        f.readline()

    print("Кулинарная книга:\n")
    pprint(cook_book, width=70, indent=0)

print()
print()

'''
def ordering_dishes(dishes, person_count, ordered_item=None):
    dishes_list = {}
    for d in dishes:
        for ing in cook_book[d]:
            ordered_item = dict(ing)
            ordered_item['количество'] = int(ordered_item['количество']) * person_count
            if ordered_item['Ингредиент'] not in dishes_list:
                dishes_list[ordered_item['Ингредиент']] = str(ordered_item['количество']) + str(ordered_item['объём в'])
                #print(dishes_list)
            else:
                dishes_list[ordered_item['Ингредиент']]['количество'] += str(ordered_item['количество'])
    return dishes_list


order_list = ordering_dishes(['Запеченный картофель', 'Омлет'], 2)


print("Обед на две персоны:\n")
print()
print("Заказ: Запеченный картофель и Омлет.\nНеобходимые ингридиенты:\n")
print()
pprint(order_list, width=65, indent=0)
'''
def ordering_dishes(dishes, person_count, ordered_item=None):
    dishes_list = {}
    for d in dishes:
        for ing in cook_book[d]:
            ordered_item = dict(ing)
            ordered_item['количество'] = int(ordered_item['количество']) * person_count
            if ordered_item['Ингредиент'] not in dishes_list:
                dishes_list[ordered_item['Ингредиент']] =   dict(list(ordered_item.items())[1:])#['количество'])
                #dishes_list[ordered_item['Ингредиент']] += ordered_item['объём в']
                #print(dishes_list)
            else:
                dishes_list[ordered_item['Ингредиент']]['количество'] += str(ordered_item['количество'])
    return   dishes_list


order_list = ordering_dishes(['Запеченный картофель', 'Омлет'], 2)

print("Обед на две персоны:\n")
print()
print("Заказ: Запеченный картофель и Омлет.\nНеобходимые ингридиенты:\n")
print()
pprint(order_list, width=65, indent=0)
