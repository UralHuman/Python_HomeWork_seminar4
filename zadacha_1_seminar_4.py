n, m = int(input("Введите значение n: ")), int(input("Введите значение m: "))

list1 = []
list2 = []
for i in range(n):
    num = int(input("list1>>> "))
    list1.append(num)
print()
for i in range(m):
    num = int(input("list2>>> "))
    list2.append(num)

set1 = set(list1)
set2 = set(list2)
intersection = set1.intersection(set2)

list3 = list(intersection)
list3.sort()
print(*list3)

