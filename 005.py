months = {
  1: 'Januar',
  2: 'Februar',
  3: 'März',
  4: 'April',
  5: 'Mai',
  6: 'Juni',
  7: 'Juli',
  8: 'August',
  9: 'September',
  10: 'Oktober',
  11: 'November',
  12: 'Dezember'   
}


print('Bitte geben Sie einen Monat ein: ')

selection = int(input())

if  selection in months.keys():
  print(months[selection])
else:
  print('Bitte Zahl zwischen einschließlich 1 und 12 angeben!')



