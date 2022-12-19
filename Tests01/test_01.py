data = [
    ['Volkswagen', 'Golf V', '2008', '8000', '154000'],
    ['Mazda', 'CX-5', '2013', '14800', '117000'],
    ['Honda', 'CR-V AWD', '2017', '22000', '57000'],
    ['BMW', '320', '2015', '14700', '124000'],
    ['BMW', 'X1', '2012', '17000', '62000'],
    ['Mercedes-Benz', 'E 220', '2009', '9300', '240000'],
    ['Volkswagen', 'Golf VI STYLE', '2011', '9700', '203000'],
    ['Mazda', '6', '2006', '5600', '218000'],
    ['Hyundai', 'Tucson LOUNGE 2009', '2008', '8899', '149000'],
    ['BMW', '520', '2013', '21700', '146000'],
    ['Toyota', 'Highlander', '2015', '28000', '120000'],
    ['Mercedes-Benz', 'E 220', '2005', '8200', '276000'],
    ['BMW', '328', '2012', '12500', '260000'],
    ['Opel', 'Astra J', '2013', '9500', '224000'],
    ['Volkswagen', 'Passat B7', '2013', '11750', '138000'],
    ['Audi', 'A6 Quattro', '2006', '8000', '28000']
]

# пишем название колонок в две строчки
columns = [['Марка', 'Модель', 'Год', 'Цена', 'Пробег'],
           ['автомобиля', '', 'выпуска', ' $', 'км']]


def print_table(data, columns, indent, max_width=100):
    # data — список списков, данные таблицы
    # columns — список списков, названия колонок таблицы
    # indent — отступ от края колонки
    # max_widt – допустимая ширина таблицы
    # max_columns — список максимальной длинны строки колонок
    # max_columns_title — список максимальной ширины колонок шапки
    # width — список ширины каждой колонки таблицы для печати

    # расчёт макимальной ширины колонок таблицы
    max_columns = []
    for col in zip(*data):
        len_el = []
        [len_el.append(len(el)) for el in col]
        max_columns.append(max(len_el))

    # вычислить максимальную длинну колонки шапки таблицы
    max_columns_title = []
    for col in zip(*columns):
        max_columns_title.append(max([len(el) for el in col]))

    # печать таблицы
    for col in columns:
        width = []
        for n, c in enumerate(col):

            # сравниваем максимальную колонку шапки с макс колонкой таблицы
            if max_columns[n] >= max_columns_title[n]:
                w = max_columns[n] + indent
                width.append(w)
            else:
                w = max_columns_title[n] + indent
                width.append(w)

            # пишем название колонок в две строки
            if sum(width) <= max_width:
                print(f'{c:^{w}}', end='')  # выравниване по ценру
            else:
                print('Ширина таблицы больше допустимого значения')
                return
        print()

    # печать разделителя шапки '='
    print(f"{'='*(sum(width))}")

    # печать тела таблицы
    for el in data:
        for n, col in enumerate(el):
            print(f'{col:>{width[n]}}', end='')  # выравнвание по правому краю
        print()


print_table(data, columns, 1, max_width=100)