perevod = {'км':1000, 'м':1, 'см':0.01, 'мм':0.001, 'mi':1609.34,'yd':0.9144}

while True:
    istochnik = input("Исходная единица (км/м/см/мм/mi/yd):").strip().lower()
    if istochnik in perevod: break
    print("Некорректный ввод данных! Доступные единицы: км, м, см, мм, mi, yd")

while True:
    cel = input("Целевая единица (км/м/см/мм/mi/yd): ").strip().lower()
    if cel in perevod: break
    print("Некорректный ввод данных! Доступные единицы: км, м, см, мм, mi, yd")

while True:
    try:
        znachenie = float(input("Значение: ").replace(',', '.'))
        break
    except ValueError:
        print("Некорректный ввод данных! Введите число")

rezultat = znachenie * perevod[istochnik] / perevod[cel]
print(f"{znachenie} {istochnik} = {rezultat:.6f} {cel}")
