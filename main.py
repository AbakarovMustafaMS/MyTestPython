import csv
Mypoints = 0
with open("MyBook.csv", "r", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
      print(row[0])
      print(row[1], row[2], row[3])
      i = input()
      if i == row[4].replace(' ', ''):
        Mypoints += 5
    print("Вы набрали " + str(Mypoints) + " баллов")
if Mypoints <= 59:
  print("Ваша оценка F(Провал)")
elif Mypoints > 59 and Mypoints <= 62:
  print("Оценка D-(Плохо)")
elif Mypoints > 62 and Mypoints <= 66:
  print("Оценка D(Плохо)")
elif Mypoints > 66 and Mypoints <= 69:
  print("Оценка D+(Плохо)")
elif Mypoints > 69 and Mypoints <= 73:
  print("Оценка C-(Средне)")
elif Mypoints > 73 and Mypoints <= 76:
  print("Оценка C(Средне)")
elif Mypoints > 76 and Mypoints <= 79:
  print("Оценка C+(Средне)")
elif Mypoints > 79 and Mypoints <= 82:
  print("Оценка B-(Хорошо)")
elif Mypoints > 82 and Mypoints <= 86:
  print("Оценка B(Хорошо)")
elif Mypoints > 86 and Mypoints <= 89:
  print("Оценка B+(Хорошо)")
elif Mypoints > 89 and Mypoints <= 93:
  print("Оценка А-(Отлично)")
elif Mypoints > 93 and Mypoints <= 100:
  print("Оценка А(Отлично)")