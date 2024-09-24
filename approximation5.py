import numpy as np
import matplotlib.pyplot as plt

# Задаем данные
x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200])
y = np.array([235,234,232,229,224,218,209,201,194,187,179,168,149,128,113,98,85,73,64,55,47,37,30,25,20,16,12,10,8,5,4,3,2,1,1,1,1,1,1,2,3,4,5,6,7,7,7,7,6,5,5,4,3,2,2,1,1,2,3,4,5,8,10,12,16,21,25,29,33,37,42,47,53,59,66,73,78,85,87,93,98,106,112,120,123,126,129,131,133,135,138,142,148,152,157,163,172,178,185,190,205])

# Выбираем случайные пять точек
random_indices = np.random.choice(len(x), size=5, replace=False)
x_subset = x[random_indices]
y_subset = y[random_indices]

# Аппроксимация методом наименьших квадратов (полином второй степени)
coefficients = np.polyfit(x_subset, y_subset, 2)
polynomial = np.poly1d(coefficients)

# Генерируем значения x для построения графика
x_fit = np.linspace(min(x), max(x), 100)
y_fit = polynomial(x_fit)

# Визуализация результатов
plt.plot(x, y, label='Исходные данные', color='blue')
plt.scatter(x_subset, y_subset, label='5 точек', color='red')
plt.plot(x_fit, y_fit, label='Аппроксимация МНК', color='red')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Аппроксимация методом наименьших квадратов по 5 точкам')
plt.show()
