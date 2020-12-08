# -*- coding: utf-8 -*-

# Дана строка.
def doWeirdThingsWithString(string):
  if len(string) <= 2:
    print('You can\'t use a string that short!')
    return

  # Сначала выведите третий символ этой строки.
  print(string[2])

  # Во второй строке выведите предпоследний символ этой строки.
  print(string[-2])

  # В третьей строке выведите первые пять символов этой строки.
  print(string[0 : 5])

  # В четвертой строке выведите всю строку, кроме последних двух символов.
  print(string[0 : len(string) - 2])

  stringWithEvenCharacters = ''
  stringWithOddCharacters = ''
  for i in range(0, len(string)): 
    if i % 2 == 0:
      # В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
      stringWithEvenCharacters += string[i]
    else:
      # В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
      stringWithOddCharacters += string[i]

  print(stringWithEvenCharacters)
  print(stringWithOddCharacters)

  # В седьмой строке выведите все символы в обратном порядке.
  reversedString = ''
  for i in reversed(range(0, len(string))):
    reversedString += string[i]
  print(reversedString)

  # В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
  reversedStringWithGaps = ''
  for i in reversed(range(0, len(string))):
    if i % 2 == 0:
      reversedStringWithGaps += string[i]
  print(reversedStringWithGaps)

  # В девятой строке выведите длину данной строки.
  print(len(string))


doWeirdThingsWithString('hello world')