n_vvod = input('введите целое число ')
n_max = 0
while int(n_vvod) >0:
    n_tek = int(int(n_vvod) % 10)
 #  print(n_tek)
    n_vvod= int(int(n_vvod) // 10)
 #  print(n_vvod)
    if n_tek >= n_max:
        n_max = n_tek
print("максимальная цифра в числе ", n_max)
