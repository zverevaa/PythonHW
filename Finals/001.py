# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.
import numpy as np
import matplotlib.pyplot as plt
x = []
y = []


for i in range(-10, 10):
    x.append(i)
for i in range(len(x)):
    y.append(5 * x[i] * x[i] + 10 * x[i] - 30)

print(f'Между точками пересечения графика функции с осью абсцисс, значение функции отрицательно')


plt.axhline(0, color='red')
plt.axvline(0, color='red')
plt.grid()
plt.plot(x, y)
plt.show()
