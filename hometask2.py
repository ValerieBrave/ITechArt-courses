# ------TASK1
def cases_rubles(c):
    if c == 1 or c % 10 == 1:
        return " рубль"
    elif 1 < c % 10 <= 4:
        return " рубля"
    else:
        return " рублей"


# -----TASK2


def cases_pennies(p):
    if p == 1 or p % 10 == 1:
        return " копейка"
    elif 1 < p % 10 <= 4:
        return " копейки"
    else:
        return " копеек"


# -----TASK3


def cases_num_mal(a):
    if a == 0:
        return " ноль "
    result = ""
    centuries = a // 100
    if a % 100 == 0 or a % 100 < 10:
        decades = 0
    else:
        decades = (a % 100) // 10
    if a % 10 == 0:
        numbers = 0
    else:
        numbers = a % 10
    if centuries != 0:
        if centuries == 1:
            result = "сто"
        elif centuries == 2:
            result = "двести"
        elif centuries == 3:
            result = "триста"
        elif centuries == 4:
            result = "четыреста"
        elif centuries == 5:
            result = "пятьсот"
        elif centuries == 6:
            result = "шестьсот"
        elif centuries == 7:
            result = "семьсот"
        elif centuries == 8:
            result = "восемьсот"
        else:
            result = "девятьсот"
    if decades != 0:
        if decades == 1 and numbers == 0:
            result += " десять"
        elif decades == 1 and numbers != 0:
            if numbers == 1:
                result += " одиннадцать"
            elif numbers == 2:
                result += " двенадцать"
            elif numbers == 3:
                result += " четырнадцать"
            elif numbers == 5:
                result += " пятнадцать"
            elif numbers == 6:
                result += " шестнадцать"
            elif numbers == 7:
                result += " семнадцать"
            elif numbers == 8:
                result += " восемнадцать"
            elif numbers == 9:
                result += " девятнадцать"
        elif decades == 2:
            result += " двадцать"
        elif decades == 3:
            result += " тридцать"
        elif decades == 4:
            result += " сорок"
        elif decades == 5:
            result += " пятьдесят"
        elif decades == 6:
            result += " шестьдесят"
        elif decades == 7:
            result += " семьдесят"
        elif decades == 8:
            result += " восемьдесят"
        else:
            result += " девяносто"
    if decades != 1 and numbers != 0:
        if numbers == 1:
            result += " один"
        elif numbers == 2:
            result += " два"
        elif numbers == 3:
            result += " три"
        elif numbers == 4:
            result += " четыре"
        elif numbers == 5:
            result += " пять"
        elif numbers == 6:
            result += " шесть"
        elif numbers == 7:
            result += " семь"
        elif numbers == 8:
            result += " восемь"
        else:
            result += " девять"
    return result


# -----TASK4

def cases_num_fem(a):
    if a == 0:
        return " ноль "
    result = ""
    centuries = a // 100
    if a % 100 == 0 or a % 100 < 10:
        decades = 0
    else:
        decades = (a % 100) // 10
    if a % 10 == 0:
        numbers = 0
    else:
        numbers = a % 10
    if centuries != 0:
        if centuries == 1:
            result = "сто"
        elif centuries == 2:
            result = "двести"
        elif centuries == 3:
            result = "триста"
        elif centuries == 4:
            result = "четыреста"
        elif centuries == 5:
            result = "пятьсот"
        elif centuries == 6:
            result = "шестьсот"
        elif centuries == 7:
            result = "семьсот"
        elif centuries == 8:
            result = "восемьсот"
        else:
            result = "девятьсот"
    if decades != 0:
        if decades == 1 and numbers == 0:
            result += " десять"
        elif decades == 1 and numbers != 0:
            if numbers == 1:
                result += " одиннадцать"
            elif numbers == 2:
                result += " двенадцать"
            elif numbers == 3:
                result += " четырнадцать"
            elif numbers == 5:
                result += " пятнадцать"
            elif numbers == 6:
                result += " шестнадцать"
            elif numbers == 7:
                result += " семнадцать"
            elif numbers == 8:
                result += " восемнадцать"
            elif numbers == 9:
                result += " девятнадцать"
        elif decades == 2:
            result += " двадцать"
        elif decades == 3:
            result += " тридцать"
        elif decades == 4:
            result += " сорок"
        elif decades == 5:
            result += " пятьдесят"
        elif decades == 6:
            result += " шестьдесят"
        elif decades == 7:
            result += " семьдесят"
        elif decades == 8:
            result += " восемьдесят"
        else:
            result += " девяносто"
    if decades != 1 and numbers != 0:
        if numbers == 1:
            result += " одна"
        elif numbers == 2:
            result += " две"
        elif numbers == 3:
            result += " три"
        elif numbers == 4:
            result += " четыре"
        elif numbers == 5:
            result += " пять"
        elif numbers == 6:
            result += " шесть"
        elif numbers == 7:
            result += " семь"
        elif numbers == 8:
            result += " восемь"
        else:
            result += " девять"
    return result


# ------TASK5

def show_sum(mon):
    print(cases_num_mal(int(mon[0])), end=" ")
    print(cases_rubles(int(mon[0])), end=" ")
    print(cases_num_fem(int(mon[1])), end=" ")
    print(cases_pennies(int(mon[1])))


money = input("Ваша сумма: ").split(",")
show_sum(money)
