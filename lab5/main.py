import numpy as np
import pandas as pd
import random
def print_r(data, dataType):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm' + "<--- " + str(dataType) + " --->" + '\033[0m')
    print(data)
    print('\033[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm' + "<--- Конец --->" + '\033[0m')


# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', 10)

# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)

# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', 30)

df = pd.read_csv('smartphones.csv')

print_r(df, "2.1 Вывод всей таблицы")

print_r(df.head(), "2.2 Вывод первых пяти строк")

print_r(df.tail(), "2.3 Вывод последних пяти строк")

print_r(df.describe(), "2.4 Получение основной статистической информации функцией describe()")

print_r(df.loc[0,'Product Name'], "2.5 Чтение ячейки по индексу строки и имени колонки")
print_r(df.iloc[0, 0], "2.5 Чтение ячейки по строке и столбцу")
print_r(df.at[0,'Product Name'], "2.5 Чтение ячейки через at")

print_r(df[10:20], "2.6 Фильтрация строк по диапазону индекса")  # возвращает строки с индексами от 10 до 19

print_r(df[df['Brand'] == 'Samsung'], "2.7 Фильтрация по условию")  # возвращает строки, в которых значение в колонке 'brand' равно 'Samsung'

# Работа с пропущенными значениями
# Для проверки, сколько пропущенных значений есть в каждой колонке, используйте функцию isnull()
print_r(df.isnull().sum(), "2.8 Подсчёт пустых значений")
# Удаление строк с пропущенными значениями
df = df.dropna()
# Заполнение пропущенных значений средним значением:
mean_value = df['Sale Price'].mean()
df['Sale Price'].fillna(value=mean_value, inplace=True)
# Добавление NaN-значений к какой-то выбранной ячейке:
df.at[0,'Product Name'] = np.nan

df['Discounted Price'] = df['Mrp'] - df['Sale Price']
print_r(df.head(), "2.9.1 Создание нового поля через выражение на базе имеющихся колонок")


def calculate_discounted_price(row):
    return row['Mrp'] - row['Sale Price']


df['Discounted Price'] = df.apply(calculate_discounted_price, axis=1)
print_r(df.head(), "2.9.2 Создание новых полей через DataFrame.apply")

df['Discounted Price'] = df['Mrp'].apply(lambda x: x - 1000)
print_r(df.head(), "2.9.3 Создание новых полей через Series.apply")

df.sort_values('Sale Price', ascending=False, inplace=True)  # сортировка по убыванию стоимости продажи
print_r(df.head(), "2.10 Сортировка по Sale Price")

print_r(df[['Sale Price', 'Mrp', 'Discount Percentage', 'Number Of Ratings', 'Number Of Reviews', 'Star Rating']].mean(), "2.11.1 Среднее значение для каждой колонки")
print_r(df[['Sale Price', 'Mrp', 'Discount Percentage', 'Number Of Ratings', 'Number Of Reviews', 'Star Rating']].max(), "2.11.2 Максимальное значение в каждой колонке")
print_r(df[['Sale Price', 'Mrp', 'Discount Percentage', 'Number Of Ratings', 'Number Of Reviews', 'Star Rating']].sum(), "2.11.3 Сумма значений в каждой колонке")

print_r(df['Brand'].value_counts(),
        "2.12 Подсчет уникальных значений в колонке")  # возвращает количество смартфонов каждого бренда

print_r(df['Ram'].unique(),
        "2.13 Вывод уникальных значений в колонке")  # возвращает массив с уникальными значениями оперативной памяти

df = df.reset_index(drop=True)  # удаление текущего индекса
df.set_index('Product Name', inplace=True)  # создание нового индекса на базе колонки 'product_name'
print_r(df.head(), "2.14 Удаление текущего индекса и создание нового на базе новой колонки")
