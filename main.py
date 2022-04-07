import matplotlib.pyplot as plt
import numpy as np

#2

x = np.arange(-4, 4, 0.01)
print(x)

plt.plot(x, x**2)
plt.plot(x, x**3)
plt.show()

v = [12, 55, 4, 32, 14]
c = [ 'r', 'g', 'b', 'c', 'm']
plt.bar( x = range(0, 5), height= v, color = c)
plt.show()

v = [12, 55, 4, 32, 14]
c = [ 'r', 'g', 'b', 'c', 'm']
explode = [0, 0, 0.2, 0, 0]
lab = [1, 2, 3, 4, 5]

plt.title('Диаграмма')

plt.pie(v, colors= c)
plt.show()

#3

l1 = [1, 2, 3]
l2 = [0.1, 0.2, 0.3]

a = np.array(l1)
b = np.array(l2)

print(a)
print(b)

#4

print(a[:2])
print(a[2:])
print(a[-1])
print(a[-3])

print(l1.extend([30, 40]))

e = np.arange(10)
print(e)

e = np.arange(10, 101)
print(e)

e = np.arange(10, 100, 10)
print(e)

print(e[e>80])

print(e.clip(40, 60))

#HW

a = np.zeros(10, dtype=int)
print(a)

a = np.ones(10, dtype=int)
print(a)

a = np.ones(10, dtype=int)
print(a * 5)

a = np.ones(10, dtype=int)
print(a * 5)

a = np.array(range(10, 51))
print(a)

a = np.array(range(10, 51, 2))
print(a)

a = np.arange(0, 9, 1).reshape((3, 3))
print(a)