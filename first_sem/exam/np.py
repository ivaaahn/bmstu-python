import numpy as np

print('Вид поля')
dt = np.dtype([('name', 'U10'), ('height', float), ('age', int)])
print(dt, '\n')

print('Исходный список')
group = [('Саша', 1.8, 16), ('Ваня', 1.85, 16), ('Никита', 1.76, 18)]
print(group, '\n')

print('Сортированный список')
a = np.array(group, dtype=dt)
print(a, '\n')

print('Отсортированный список по росту')
print(np.sort(a, order='height'), '\n\n')


print('Отсортированный список по имени')
print(np.sort(a, order='name'), '\n\n')

print('Отсортированный список по возрасту и по росту, при равенстве возраста')
print(np.sort(a, order=['age', 'height']), '\n\n')

print('Только имена')
print(a['name'])

# print('Другой вариант задания данных и no name')
#
# a = np.array([('Саша', 1.8, 16), ('Ваня', 1.85, 16), ('Никита', 1.76, 18)],
#              dtype=[('name', ' '), ('height', float), ('age', int)])

# a = np.array([[2, 6], [5, 2]])
# print(a, end='\n\n')
#
# a = np.sort(a, axis=None)
# print(a)
