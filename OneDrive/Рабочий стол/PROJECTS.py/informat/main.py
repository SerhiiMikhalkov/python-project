########################### Завдання 1 ###################################################

num = [39, 10, 60, 3, 35]

# Перший спосіб

min_number = min(num)
max_number = max(num)

# Другий спосіб

Min = num[0]
Max = num[0]

for i in range(5):
    if Min>num[i]:
        Min = num[i]
    elif Max<num:
        Max = num(i)

print("Мінімальне: ", Min)
print("Максимальне: ", Max)

############################ Завдання 2 ###################################################

num = [354, 33, 70, 40, 9, 21, 45]

Min = num[0]
Max = num[0]

for i in range(7):
    if Min>num[i]:
        Min = num[i]
    elif Max<num:
        Max = num(i)

print("Мінімальне: ", Min)
print("Максимальне: ", Max)

########################### Завдання 3 ###################################################

ukr = [2201, 1362, 806, 1053] # Дніпро, Дністер, Південний Буг, Сіверський Донець
fra = [1020, 776, 522, 522] # Луара, Сена, Гаронна, Рона

total_ukr = sum(ukr)
total_fra = sum(fra)

if total_ukr > total_fra:
    print("Загальна довжина річок України більша на", total_ukr - total_fra, "км")
elif total_fra > total_ukr:
    print("Загальна довжина річок Франції більша на", total_fra - total_ukr, "км")
else:
    print("Загальна довжина річок в Україні та Франції рівна і складає", total_ukr, "км")
