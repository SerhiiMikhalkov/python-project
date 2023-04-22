areas = []

for i in range(6):
    area = float(input("Введіть площу міста: "))
    areas.append(area)

total_area = sum(areas)

print("Загальна площа: ", total_area)
