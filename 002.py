students     = ['Torben', 'Tamara', 'Theodor', 'Tina', 'Toni']
age          = [16,       17,       18,        19,     20]
parent_agree = [False,    True,     False,     False,  False]

data = list(zip(students, age, parent_agree))


print("These students may watch the movie")
for tupel in data:
  if tupel[1] >= 18 or tupel[2]:
    print(tupel[0])