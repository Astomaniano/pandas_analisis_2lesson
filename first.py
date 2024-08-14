import pandas as pd
''' СТАНДАРТНЫЕ ОТКЛОНЕНИЯ:
data = {
    'Набор А': [85, 90, 95, 100, 105],
    'Набор Б': [70, 80, 95, 110, 120]
}

df = pd.DataFrame(data)

stdA = df['Набор А'].std()
stdB = df['Набор Б'].std()

print(f'Стандартное отклонение для Набора А: {stdA}')
print(f'Стандартное отклонение для Набора Б: {stdB}')
'''

data = {
    'Age': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
    'Salary': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000]
}

df = pd.DataFrame(data)

print(df.describe())

print(f'Средний возраст: {df["Age"].mean()}')
print(f'Медианный возраст: {df["Age"].median()}')
print(f'Стандартное отклонение возраста: {df["Age"].std()}')

print(f'Средняя зарплата: {df["Salary"].mean()}')
print(f'Медианная зарплата : {df["Salary"].median()}')
print(f'Стандартное отклонение зп: {df["Salary"].std()}')