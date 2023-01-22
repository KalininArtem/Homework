with open('Homework_7.1_data.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        dish = i.strip()
        dish_count = int(file.readline())
        ingredients = []
        for n in range(dish_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish] = ingredients

    # Простой вывод cook_book
    print(cook_book)

    # Пригодный для чтения cook_book
    for key in cook_book: #
        print(f'{key}:')
        for i in range(len(cook_book[key])):
            print(cook_book[key][i])

