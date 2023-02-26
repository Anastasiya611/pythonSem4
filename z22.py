# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите n: "))
m = int(input("Введите m: "))
list_n = []
list_m = []
for element_n in range(1, n+1):
    element_n = int(input("Введите число для списка n: "))
    list_n.append(element_n)

for element_m in range(1, m+1):
        element_m = int(input("Введите число для списка m: "))
        list_m.append(element_m)
print (list_n,list_m)
new_list = []
if len(list_n) > len(list_m):
    for i in range (len(list_n)):
        if list_n[i] in list_m:
            new_list.append(list_n[i])
            i+=1
else:
    for j in range (len(list_m)):
        if list_m[j] in list_n:
            new_list.append(list_m[j])
            j+=1
result = set(new_list)
print (sorted(result))