import os
from pprint import pprint
# with open('recipes.txt', 'w', encoding='utf-8') as f:
#     f.write('Омлет\n3\nЯйцо | 2 | штука\nМолоко | 100 | мл\nПомидор | 2 | шт\n\n')
# with open('recipes.txt', 'a', encoding='utf-8') as f:
#     f.write('Утка по-пекински\n4\nУтка | 1 | шт\nВода | 2 | л\nМед | 3 | ст.л\nСоевый соус | 60 | мл\n\n')
#     f.write('Запеченный картофель\n3\nКартофель | 1 | кг\nЧеснок | 3 | зубч\nСыр гауда | 100 | г\n\n')
#     f.write('Фахитос\n5\nГовядина | 500 | г\nПерец сладкий | 1 | шт\nЛаваш | 2 | шт\nВинный уксус | 1 | ст.л\nПомидор | 2 | шт\n\n')
def read_cookbook():
    file_pach = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book = {}
    with open(file_pach, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ingr_list = []
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ingr_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ingr_list
        return cook_book
cook_book = read_cookbook()
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                list_req_ingr = {}
                if  ings['ingredient_name'] not in ingr_list:
                    list_req_ingr['measure'] = ings['measure']
                    list_req_ingr['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = list_req_ingr
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count
        else:
            print(f'\n"Такого блюда нет!"\n')
    return ingr_list
pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))