num_kust = int(input("Введите колличество кустов: "))

my_dict = {}

for i in range(1, num_kust + 1):
    my_dict[i] = int(input(f"Введите колличество ягод на кусте {i} :"))
print(my_dict)

nomer_ku = int(input("Номер куста>> "))

if my_dict.get(nomer_ku + 1) == None:
    print(
        my_dict.get(nomer_ku - len(my_dict) + 1)
        + my_dict.get(nomer_ku)
        + my_dict.get(nomer_ku - 1)
    )

if my_dict.get(nomer_ku - 1) == None:
    print(
        my_dict.get(nomer_ku + len(my_dict) - 1)
        + my_dict.get(nomer_ku)
        + my_dict.get(nomer_ku + 1)
    )

if my_dict.get(nomer_ku - 1) != None and my_dict.get(nomer_ku + 1) != None:
    print(
        my_dict.get(nomer_ku - 1) 
        + my_dict.get(nomer_ku) 
        + my_dict.get(nomer_ku + 1))
