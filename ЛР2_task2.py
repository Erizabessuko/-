salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

def calculate_money_capital(salary, spend, increase, months=10):
    total_needed = 0  # Общая сумма, необходимая для покрытия расходов

    for month in range(1, months + 1):
        # Если это не первый месяц, увеличиваем расходы на 5%
        if month > 1:
            spend *= (1 + increase)

        # Расходы текущего месяца
        total_needed += spend

    # Необходимая подушка безопасности, чтобы протянуть 10 месяцев
    money_capital = total_needed - (salary * months)

    return round(max(0, money_capital))  # Округляем и возвращаем минимум 0

result = calculate_money_capital(salary, spend, increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {result}")