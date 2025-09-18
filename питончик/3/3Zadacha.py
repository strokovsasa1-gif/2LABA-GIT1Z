god = int(input("Введите год: "))

if (god % 400 == 0) or (god % 100 != 0 and god % 4 == 0):
    print(f"{god} год - високосный")
else:
    print(f"{god} год - не високосный")
