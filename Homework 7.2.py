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


    def shop_list_func(dishes, person_count, cook_book, ans_quantity_dishes):
        shop_list = {}
        shop_list_per = []
        for dis in range(ans_quantity_dishes):
            shop_list_per.append(cook_book[dishes[dis]])
        for step in range(len(shop_list_per)):
            # print(shop_list_per[step])
            for step_two in range(len(shop_list_per[step])):
                # print(shop_list_per[step][step_two])
                shop_list[shop_list_per[step][step_two]['ingredient_name']] = {
                    'measure': shop_list_per[step][step_two]['measure'],
                    'quantity': int(shop_list_per[step][step_two]['quantity']) * person_count
                    }
        #Вывод строкой
        # print(shop_list)

        #Вывод списком
        for key in shop_list:
            print(f'{key}: {shop_list[key]}')

    #Вариант с ручным вводом
    # dishes = []
    # ans_quantity_dishes = int(input('Введите количество приготавлиемых блюд:'))
    # for ans in range(ans_quantity_dishes):
    #     ans_dishes = input('Введите название блюда: ')
    #     dishes.append(ans_dishes)
    # person_count = int(input('Введите количестов персон: '))

    #Вариант с фиксированным вводом
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    ans_quantity_dishes = 2
    shop_list_func(dishes, person_count, cook_book, ans_quantity_dishes)