# Задача №57. Решение в группах
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

import pandas as pd
# 1
df = pd.read_csv('california_housing_test.csv')
# 2
print(df.shape)
# 3
print(df.dtypes)


# Задача №59. Решение в группах
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000

# 1
print(df.isnull().sum())
# 2
print(df.loc[df['median_income'] < 2, ['median_house_value']])
# 3
print(df[['longitude','latitude']])
# 4
print(df[(df['housing_median_age'] < 20) & (df['median_house_value']) > 70000])

# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

# 1
print(df['median_house_value'].max())
print(df['median_house_value'].min())
# 2
print(df.loc[df['median_income'] == 3.1250, 'median_house_value'].max())
# 3
print(df.loc[df['median_house_value'].idxmin(),'population'].max())