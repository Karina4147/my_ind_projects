print("Расчет индекса массы тела")

dict_value_imt = {
    "м": {
        24: [20, 25],
        34: [21, 26],
        44: [22, 27],
        54: [23, 28],
        64: [24, 29],
        99: [25, 30]
          },
    "ж": {
        24: [19, 24],
        34: [20, 25],
        44: [21, 26],
        54: [22, 27],
        64: [23, 28],
        99: [24, 29]
    }
}
while True:
    choise = input("""Выбери действие:
        1 - рассчитать индекс массы тела
        2 - закончить программу 
        """)
    if choise == '1':
        while True:
            a = int(input("Введите возраст: "))
            if 0 > a > 100:
                print("Возраст должен быть больше 0 и меньше 100")
                continue
            break
        while True:
            b = str(input("Введите пол ж/м: "))
            break
        while True:
            c = float(input("Введите рост в метрах (например 1.70): "))
            break
        while True:
            d = float(input("Введите вес в кг: "))
            if d < 0:
                print("Вес должен быть больше 0")
                continue
            break
        imt = round(d / c ** 2, 2)

        for key, value in dict_value_imt[b].items():
            if a < key:
                if value[0] <= imt <= value[-1]:
                    print("Вес в норме")
                elif imt < value[0]:
                    delta = round((value[0] - imt) * c ** 2, 2)
                    print(f'"Недостаточный вес, до нормы необходимо добавить вес на {delta} кг до {d + delta}"')
                else:
                    delta = round((value[-1] - imt) * c ** 2, 2)
                    print(f'"Избыточный вес, до нормы необходимо уменьшить вес на {delta} кг до {d + delta}"')
                break
    else:
        break

print("Программа завершена")



