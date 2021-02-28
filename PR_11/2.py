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

  print(', '.join(list(map(str, tempArr))))
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

# 143. Известно целое число N и набор из N прямоугольников, заданных своими сторонами – парами чисел (a, b). Найти минимальную площадь прямоугольника из данного набора.
def do143rdExercise(rectanglesDimensionsArray):
  rectanglesAreas = list(map(lambda dimensionsTuple: (dimensionsTuple[0] + dimensionsTuple[1]) * 2, rectanglesDimensionsArray))

  print(sorted(rectanglesAreas)[0])

do143rdExercise([(2, 3), (4, 5)])

# 173. Известно целое число N (> 1), а также первый член A и разность D арифметической прогрессии. Сформировать и вывести массив размера N, содержащий N первых членов данной прогрессии
def do173rdExercise(outputArrayLength, firstProgressionNumber, progressionDifference):
  if outputArrayLength <= 1:
    print('Parameter is invalid')
    return

  result = [firstProgressionNumber]

  for i in range(1, outputArrayLength):
    result.append(firstProgressionNumber + (i * progressionDifference))

  print(result)

do173rdExercise(10, 1, 2)

# 227. Дан целочисленный массив A размера N. Переписать в новый целочисленный массив B того же размера вначале все элементы исходного массива с четными номерами, затем – с нечетными
def do227thExercise(inputArray):
  evenNumbersFromInputArray = []
  oddNumbersFromInputArray = []

  for i in range(0, len(inputArray)):
    if i % 2 == 0:
      evenNumbersFromInputArray.append(inputArray[i])
    else:
      oddNumbersFromInputArray.append(inputArray[i])

  result = evenNumbersFromInputArray + oddNumbersFromInputArray

  return result

print(do227thExercise([1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 7]))

# 290. Дан целочисленный массив размера N, содержащий по крайней мере одну серию, длина которой больше 1. Преобразовать масиив, уменьшив каждую его серию на один элемент (определение серии Известно в задании 286).
def do290thExercise(inputArray):
  result = [inputArray[0]]

  for i in range(1, len(inputArray)):
    if inputArray[i] == inputArray[i - 1]:
      if i + 1 >= len(inputArray):
        continue
      elif inputArray[i] != inputArray[i + 1]:
        continue
      else:
        result.append(inputArray[i])
    else:
      result.append(inputArray[i])

  return result

print(do290thExercise([0, 1, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 8, 8, 8]))

# 330. Известна матрица размера M х N. Для каждого столбца матрицы найти произведение его элементов.
def do330thExercise(inputMatrix):
  columns = []

  for i in range(0, len(inputMatrix)):
    columns.append([])

  for i in range(0, len(inputMatrix)):
    for j in range(0, len(inputMatrix[i])):
      columns[j].append(inputMatrix[i][j])

  result = list(map(lambda columnValues: reduce((lambda x, y: x * y), columnValues), columns))

  return result

print(do330thExercise([
  [1, 2, 3],
  [2, 3, 1],
  [4, 4, 4]
]))
      

# 381. Известна строка, изображающая десятичную запись целого положительного числа. Вывести строку, изображающую двоичную запись этого же числа.
def do381stExercise(stringWithDecimalNumber):
  decimalNumber = int(stringWithDecimalNumber)

  return bin(decimalNumber)[2:]

print(do381stExercise('2'))

# 413. Известна строка-предложение с избыточными пробелами между словами. Преобразовать ее так, чтобы между словами был ровно один пробел.
def stringWithoutRedundantSpaces(inputString):
  previousChar = ''
  resultString = ''
  
  for character in inputString:
    if previousChar == ' ' and character == ' ':
      continue

    previousChar = character
    resultString += character

  return resultString

print(stringWithoutRedundantSpaces('hello    world    here i   am'))