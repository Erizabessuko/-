numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Сначала находим сумму всех элементов списка, кроме пропущенного
elements_sum = 0
elements_count = 0
for num in numbers:
    if num is not None:
        elements_sum += num
        elements_count += 1

# Затем находим среднее арифметическое всех элементов
average = elements_sum / (elements_count + 1)

# Заменяем пропущенный элемент на найденное среднее арифметическое
for i, num in enumerate(numbers):
    if num is None:
        numbers[i] = average
        break

# Выводим измененный список
print("Измененный список:", numbers)