import numpy as np


def power_method(matrix, initial_guess, tolerance=1e-4, max_iterations=5):
    n = matrix.shape[0]

    # Начальное приближение для собственного вектора
    x = initial_guess / np.linalg.norm(initial_guess)

    # Начальное значение собственного значения
    eigenvalue_old = 0.0
    eigenvalue = 1.0

    iteration = 0

    while np.abs(eigenvalue - eigenvalue_old) > tolerance and iteration < max_iterations:
        eigenvalue_old = eigenvalue
        x = np.dot(matrix, x)
        x /= np.linalg.norm(x)
        eigenvalue = np.dot(x, np.dot(matrix, x))
        iteration += 1

    return eigenvalue, x, iteration


# Ввод количества матриц
num_matrices = int(input("Введите количество матриц: "))

for matrix_num in range(num_matrices):
    print(f"Матрица {matrix_num + 1}:")

    # Ввод размерности матрицы
    n_str = input("Введите размерность матрицы (строки столбцы, разделенные пробелом): ")
    n_rows, n_cols = map(int, n_str.split())

    # Ввод элементов матрицы
    print("Введите элементы матрицы:")
    matrix = np.zeros((n_rows, n_cols))
    for i in range(n_rows):
        row_input = input(f"Введите элементы {i + 1} строки через пробел: ")
        row_values = [float(val) for val in row_input.split()]
        if len(row_values) != n_cols:
            print(f"Неверное количество элементов в строке {i + 1}. Повторите ввод.")
            exit()
        matrix[i, :] = row_values

    # Ввод вектора начального приближения
    initial_guess = []
    print("Введите элементы вектора начального приближения:")
    for i in range(n_rows):
        initial_guess.append(float(input(f"Элемент [{i + 1}]: ")))
    initial_guess = np.array(initial_guess)

    # Вычисление максимального собственного значения
    max_eigenvalue, max_eigenvector, max_iterations = power_method(matrix, initial_guess)
    max_eigenvalue = round(max_eigenvalue, 4)
    max_eigenvector = [round(x, 4) for x in max_eigenvector]
    print(f"Максимальное собственное значение: {max_eigenvalue}")

    # Вычисление минимального собственного значения
    min_eigenvalue, min_eigenvector, min_iterations = power_method(np.linalg.inv(matrix), initial_guess)
    min_eigenvalue = round(1 / min_eigenvalue, 4)
    min_eigenvector = [round(x, 4) for x in min_eigenvector]
    print(f"Минимальное собственное значение: {min_eigenvalue}")

    max_eigenvector = np.array(max_eigenvector)
    min_eigenvector = np.array(min_eigenvector)

    # Вычисление максимальной невязки
    residual_max = np.linalg.norm(np.dot(matrix, max_eigenvector) - max_eigenvalue * max_eigenvector)

    # Вычисление минимальной невязки
    residual_min = np.linalg.norm(
        np.dot(np.linalg.inv(matrix), min_eigenvector) - (1 / min_eigenvalue) * min_eigenvector)

    print(f"Максимальная невязка: {residual_max:.4e}")
    print(f"Минимальная невязка: {residual_min:.4e}")
    print()
