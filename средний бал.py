# написть словарь, где ключем будет имя ученика, а значением его средний бал оценок.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 4, 5]] # список оценок
print(type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # множество неупорядочное последовательность имен

print(type(students))
m = sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])
print(m) #
s = sorted(students) # метод sorted позволяет отсортировать имена и расположить с алфавитном порядке
print(s)
d = dict(zip(s, m)) # метод zip объединяет 2х псисков, первых элементов
print(d)
