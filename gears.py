#! /usr/bin/env python3.6

import math

# Межосевое расстояние
# Возвращает a, если смещения нет и aw, если смещение есть
def interaxis_distance(m, q, z2, x):
    if x == 0:
        return ((0.5 * m) * (q + z2))
    else:
        return ((0.5 * m) * (q + z2 + (2 * x)))

# Начальный угол подъёма витков червяка - гамма w
def ev_angle_initial(z1, q, x):
    formula = z1 / (q + (2 * x))
    return math.atan(formula)

# Делительный угол подъёма витков червяка - гамма
def ev_angle_divisory(z1, q):
    formula = z1 / q
    return math.atan(formula)

# Делительный диаметр червяка - d1
def worm_divisory_diameter(m, q):
    return m * q

# Делительный диаметр червячного колеса - d2
def gear_divisory_diameter(m, z2):
    return m * z2

# Наибольший возможный диаметр колеса - dae2
def maximum_gear_diameter(da2, m, z1):
    return (da2 + ((6 * m)/(z1 + 2)))

# Возвращает число витков червяка в зависимости от передаточного
# числа
def get_z1(u):
    z1 = 1
    if u >= 8 and u <= 14:
        z1 = 4
    if u >= 15 and u <= 30:
        z1 = 2
    if u > 30:
        z1 = 1
    return z1

# Возвращает z2 = число зубьев червячного колеса
def get_z2(z1, u):
    z2 = z1 * u
    return round(z2)

# Примерное значение коэффициента диаметра червяка - q
def get_q(a, m, z2):
    # qmin - минимально допустимое значение q из условия жёсткости червяка
    qmin = 0.212 * z2
    q = (((2 * a) / m) - z2)
    return q

# Рекомендуемые сочетания значений модуля m и коэффициента диаметра
# червяка q по ГОСТ 19672-74
def recommend_q(m):
    q_list1 = [8, 10, 12.5, 16, 20]
    q_list2 = [8, 10, 12.5, 14, 16, 20]
    q_list3 = [8, 10, 12.5, 16]

    m_list1 = [2.5, 3.15, 4, 5]
    m_list2 = [6.3, 8, 10, 12.5]
    m_list4 = [16]

    if m in m_list1:
        return q_list1
    if m in m_list2:
        return q_list2
    if m in m_list3:
        return m_list3
    return None

def main():
    # Передаточное число теоретическое
    utheor = 8
    print("utheor {}".format(utheor))
    # Число витков червяка
    z1 = get_z1(utheor)
    print("z1 {}".format(z1))
    # Число зубьев передачи
    z2 = get_z2(z1, utheor)
    print("z2 {}".format(z2))
    # Передаточное число фактическое
    ufact = z2 / z1
    print("ufact {}".format(ufact))
    # Отклонение от заданного передаточного числа, %
    udelta = ((abs((ufact - utheor)) / utheor) * 100)
    print("udelta {}".format(udelta))
    if udelta > 4:
        print("Должно быть <4 для одноступенчатых редукторов")
    if udelta > 8:
        print("Должно быть <8 для двухступенчатых редукторов")
    # Модуль
    m = 2.5
    print("m {}".format(m))
    # Коэффициент диаметра червяка (примерный)
    q = 4
    print("q {}".format(q))
    # Коэффициент смещения червяка
    x = 0
    print("x {}".format(x))
    d2 = gear_divisory_diameter(m, z2)
    print ("d2 {}".format(d2))
    da2 = (d2 + (2 * (1 + x) * m))
    print("da2 {}".format(da2))
    dae2 = maximum_gear_diameter(da2, m, z1)
    print("dae2 {}".format(dae2))

if __name__ == '__main__':
    main()

