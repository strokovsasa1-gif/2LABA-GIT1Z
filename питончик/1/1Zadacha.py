AB = float(input("Введите длину стороны AB: "))
BC = float(input("Введите длину стороны BC: "))
CA = float(input("Введите длину стороны CA: "))

if (AB + BC > CA) and (BC + CA > AB) and (CA + AB > BC):

    Perimeter = (AB + BC + CA) 
    p = Perimeter / 2
    Ploshad = (p * (p - AB) * (p - BC) * (p - CA)) ** 0.5

    print(f"{Ploshad:.2f}")

else: print("Такого треугольника не существует!")
