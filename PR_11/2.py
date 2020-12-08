# -*- coding: utf-8 -*-

import math 

# 29. Известно значение угла a в градусах (0 < a < 360). Определить значение того же угла в радианах, учитывая, что 180 градусов = pi радианов
def getRadiansFrom(degrees):
  return math.radians(degrees)

print(getRadiansFrom(180))

# 47. Известны два числа. Вывести порядковый номер меньшего из них
def getSerialNumberOfSmallest(numberA, numberB):
  tempArr = [numberA, numberB]
  return tempArr.index(min(tempArr)) + 1
print(getSerialNumberOfSmallest(20, 1))

# 72. Известны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа, расположенные между A и B (включая сами числа A и B), а также количество N этих чисел
def do72ndExercise(numberA, numberB):
  if numberA >= numberB:
    print('You\'re not allowed to use these numbers!')
    return
  
  tempArr = []

  for i in range(numberA + 1, numberB):
    tempArr.append(i)

  tempArr.sort()

  print(', '.join(list(map(str,tempArr))))
  print(len(tempArr))

do72ndExercise(5, 14)

# 112. Известны положительные числа A и B (A > B). На отрезке длины A размещено максимально озможное кол-во отрезков длины B (без наложений). Не используя операции умножения и деления, найти длину незанятой части отрезка A
def do112thExercise(numberA, numberB):
  if numberA < 0 or numberB < 0 or numberA <= numberB :
    print('You\'re not allowed to use these numbers!')
    return

  temp = numberA

  while temp - numberB >= 0:
    temp -= numberB

  return temp

print(do112thExercise(10, 3))

# 143.

# 173.

# 227.

# 290.

# 330.

# 381.

# 413.