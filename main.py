print('\nЗадача 4. Театр')

# Планируется построить театр под открытым небом,
# но для начала нужно хотя бы примерно понять сколько должно быть рядов,
# сидений в них и какое лучше сделать расстояние между рядами.
#
# Напишите программу,
# которая получает на вход кол-во рядов, сидений и свободных метров между рядами,
# а затем выводит примерный макет театра на экран.

# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======

rows = int(input('Введите кол-во рядов: '))
sittings = int(input('Введите кол-во сидений ряду: '))
distance = int(input('Введите кол-во метров между рядами: '))

for i in range (rows):
  print('=' * sittings, '*' * distance, '=' * sittings)
