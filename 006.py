print('Gib ein Jahr an:')

year = int(input())


if year % 4 == 0 and year % 100 != 0:
  print(str(year) + ' ist ein Schaltjahr')
else:
  print(str(year) + ' ist kein Schaltjahr')