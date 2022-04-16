def compiling_book(file_path: str) -> dict:
    ''' Считывает файл с рецептами

        (str) -> dict

        file_path - Название файла в текущем каталоге или путь до файла

        Для корректной работы функци список рецептов должен храниться в
        отдельном текстовом файле в "utf-8" кодировке в следующем формате:

        Название блюда
        Количество ингредиентов в блюде
        Название ингредиента | Количество | Единица измерения
        Название ингредиента | Количество | Единица измерения

        Возвращает структурированный словарь
    '''
    book = {}
    with open(file_path, encoding="utf-8") as source_file:
        for dish in source_file:
            if dish.strip() == '':
                continue
            else:
                book[dish.strip()] = []
                quantity_ingredients = int(source_file.readline().strip())
                for num in range(quantity_ingredients):
                    ingredient = {}
                    source_ingr = source_file.readline().strip().split(' | ')
                    ingredient['ingredient_name'] = source_ingr[0]
                    ingredient['quantity'] = int(source_ingr[1])
                    ingredient['measure'] = source_ingr[2]
                    book[dish.strip()] += [ingredient]
    return book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    ''' Составляет структурированный словарь с необходимыми ингредиентами и их количеством,
        для приготовления указанных блюд на указанное количество персон

        (list, int) -> dict

    dishes - список из блюд, которые нас интересуют. [str, str, ...]
    person_count: - количество персон, на которое необходимо произвести расчет

    Для корректной работы необходима глобальная переменная "__cook_book" - являющаяся
    структурированным словарем, содержащим список рецептов.
    Составление словаря возможно посредством функции compiling_book().
    '''
    ingredients = {}
    for dish in dishes:
        if dish not in __cook_book.keys():
            print(f'В меню нет блюда {dish}')
        else:
            for ingredient in __cook_book[dish]:
                if ingredient['ingredient_name'] in ingredients.keys():
                    ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    ingredients[ingredient['ingredient_name']] = dict(measure=ingredient['measure'],
                                                                      quantity=ingredient['quantity'] * person_count)
    return ingredients


file_path = "recipes.txt"
__cook_book = compiling_book(file_path)
print('\n', __cook_book, '\n')
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
