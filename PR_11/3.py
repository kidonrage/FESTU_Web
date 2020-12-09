# -*- coding: utf-8 -*-

# Создать класс Triangle для представления трегуольника. Поля данных должны включать углы и стороны. 
# Требуется реализовать операции: получения и изменения полей данных, вычисления площади, вычисления периметра, вычисления высот, а также определения вида треугольника (равносторонний, равнобедренный или прямоугольный)

import math

class Triangle(object):
    def __init__(self, a, b, c):
        self.setSides(a, b, c)

    def setSides(self, a, b, c):
      if a + b <= c or a + c <= b or b + c <= a:
          raise RuntimeError('Sides of triangle you trying to create are invalid')

      angleAB = math.degrees(math.acos((b * b + c * c - a * a) / (2.0 * b * c)))
      angleBC = math.degrees(math.acos((c * c + a * a - b * b) / (2.0 * c * a)))
      angleCA = 180 - angleAB - angleBC

      self.angleAB = angleAB
      self.angleBC = angleBC
      self.angleCA = angleCA
      self.a = a
      self.b = b
      self.c = c

    def setAngles(self, angleAB, angleBC, angleCA):
        if angleAB + angleBC + angleCA != 180 or angleAB == 0 or angleBC == 0 or angleCA == 0:
          raise RuntimeError('Angles of triangle you trying to create are invalid')

    def getAToBCHeight(self):
      area = self.area()
      return (2 * area) / self.a
    
    def getBToCAHeight(self):
      area = self.area()
      return (2 * area) / self.b

    def getCToABHeight(self):
      area = self.area()
      return (2 * area) / self.c
 
    def area(self):
        p = float(self.perimeter()) / 2
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area
    
    def perimeter(self):
        return self.a + self.b + self.c

    def getType(self):
      if self.angleAB == 90 or self.angleBC == 90 or self.angleCA == 90:
        return 'Right triangle'

      if self.a == self.b == self.c:
        return 'Equilateral triangle'

      if self.a == self.b or self.b == self.c or self.c == self.a:
        return 'Isosceles triangle'

      return "Just a triangle"

testTriangle = Triangle(10, 4, 7)
print(testTriangle.area())
print(testTriangle.getAToBCHeight())
print(testTriangle.getBToCAHeight())
print(testTriangle.getCToABHeight())
print(testTriangle.getType())