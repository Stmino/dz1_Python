#Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.

x1=int(input('enter x1 '))
y1=int(input('enter y1 '))
x2=int(input('enter x2 '))
y2=int(input('enter y2 '))
import math
distance = float(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
print(distance)

