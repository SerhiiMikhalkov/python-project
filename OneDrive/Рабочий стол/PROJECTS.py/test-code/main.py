products = {
    'Ноутбуки и компьютеры': {
        'Ноутбуки': {
            'Ноутбук Lenovo V14 G2 ITL': {
                'Цена': 16999,
                'Диагональ экрана': 14,
                'Разрешение': '1920x1080'
                },
            'Ноутбук HP': {
                'Цена': 10000,
                'Диагональ экрана': 12,
                'Разрешение': '1000x1000'
                }
            },
'Компьютеры': {
'Компьютер Razor': {
'Цена': 32000,
'Видеокарта': 'GeForce GTX 1060',
'Процессор': 'Intel Core i5'
},
'Компьютер TrustGaming': {
'Цена': 20000,
'Видеокарта': 'GeForce GTX 750',
'Процессор': 'Intel Core i3'
}
}
},
'Бытовая техника': {
'Стиральные машины': {
'Стиральная машина узкая GORENJE WNEI': {
'Цена': 14499,
'Габариты': '85 х 60 х 46.5 см',
'Класс энергопотребления': 'А+++',
'Тип двигателя': 'Инверторный'
},
'Стиральная машина с сушкой WHIRLPOOL': {
'Цена': 25199,
'Габариты': '84.5 х 59.5 х 54 см',
'Класс энергопотребления': 'А',
'Тип двигателя': 'Инверторный'
}
}
}
}

counter = 0
category_list = {}
for category in products:
counter += 1
category_list[counter] = category
print(f"{counter}: {category}")

selected_category = int(input('Укажите номер категории: '))
subcategories = products[category_list[selected_category]]

counter = 0
subcategory_list = {}
for subcategory in subcategories:
counter += 1
subcategory_list[counter] = subcategory
print(f"{counter}: {subcategory}")

selected_subcategory = int(input('Укажите номер подкатегории: '))
selected_subcategory = subcategory_list[selected_subcategory]
products = subcategories[selected_subcategory]
print(products)

# ylliqxw