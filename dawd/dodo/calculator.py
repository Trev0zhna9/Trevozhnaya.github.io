def currency_converter(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,    # Доллар как база
        'EUR': 0.85,   # Евро
        'RUB': 75.0,   # Рубли
        'JPY': 110.0,  # Йены
        'UAH': 41.42,  # Гривня
        'AED': 3.67,   # Дирхам
        'TRY': 38.02,  # Лира
        'GBP': 0.75    # Фунт стерлингов
    }

    if from_currency in rates and to_currency in rates:
        amount_in_usd = amount / rates[from_currency]
        converted_amount = amount_in_usd * rates[to_currency]
        return converted_amount
    else:
        return "Ты ввел какую-то фигню, таких валют нет!"


def main():
    while True:
        print("1. Конвертация валют (доллары, евро, рубли и тд)")
        print("2. Выход (если посчитал курс валют и ты в теме)")
        choice = input("Введи номер опции (1 или 2): ")

        if choice == '1':
            print("\nТы выбрал конвертацию валют!")
            amount = float(input("Введи сумму: "))
            from_currency = input("Из какой валюты (USD, EUR, RUB, JPY, UAH, AED, TRY, GBP): ")
            to_currency = input("В какую валюту (USD, EUR, RUB, JPY, UAH, AED, TRY, GBP): ")
            result = currency_converter(amount, from_currency, to_currency)
            print(f"Ответ: {result}")

        elif choice == '2':
            print("Пока! Программа закрывается, иф ай луз ит ол, луз ит олл. луз ит ол")
            break

        else:
            print("Ты ввел какую-то фигню, выбери нормально из меню!")

if __name__ == "__main__":
    main()