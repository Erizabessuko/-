money_capital = 20000  # Подушка безопасности
salary = 5000           # Ежемесячная зарплата
spend = 6000            # Траты за первый месяц
increase = 0.05             # Ежемесячный рост цен

def financial_planning(money_capital, salary, spend, increase):
    months = 0  # Количество месяцев, на которые хватает средств
    budget = money_capital  # Начальный бюджет - финансовая подушка безопасности

    while budget + salary >= spend:  # Пока есть средства, чтобы покрыть расходы
        budget += salary  # Добавляем зарплату в бюджет
        budget -= spend   # Вычитаем текущие расходы

        months += 1  # Увеличиваем счетчик месяцев

        # Увеличиваем расходы на 5% начиная со второго месяца
        spend *= (1 + increase)

    return months

result = financial_planning(money_capital, salary, spend, increase)
print(f"Количество месяцев, которое можно протянуть без долгов: {result}")