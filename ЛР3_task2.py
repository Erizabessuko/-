def find_common_participants(group1, group2, delimiter=','):
    # Разделяем строки по указанному разделителю и преобразуем в множества
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим пересечение двух множеств (общих участников)
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)

group1 = "Иванов,Петров,Сидоров"
group2 = "Петров,Сидоров,Смирнов"
common = find_common_participants(group1, group2)
print(common)