# Параметры
disk_capacity_mb = 1.44  # емкость дискеты в мегабайтах
pages_per_book = 100      # количество страниц в книге
lines_per_page = 50       # количество строк на странице
chars_per_line = 25       # количество символов в строке
bytes_per_char = 4        # байты на один символ

# Расчет объема одной книги
chars_per_book = pages_per_book * lines_per_page * chars_per_line  # общее количество символов в книге
book_size_bytes = chars_per_book * bytes_per_char  # размер книги в байтах

# Преобразование емкости дискеты в байты
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024  # 1 Мб = 1024 * 1024 байт

# Расчет количества книг, которые можно поместить на дискету
number_of_books = int(disk_capacity_bytes / book_size_bytes)

# Вывод результата
print(f"Количество книг, помещающихся на дискету: {number_of_books}")