immutable_var = True, 12.2, 'Str', 5
print('Immutable tuple:', immutable_var)
# immutable_var[0] = False  Ошибка: Тип переменной 'tuple' не поддерживает изменение
mutable_list = ['var', 24, 98, False, 'line']
mutable_list[1] = 'change'
mutable_list[3] = 12
print('Mutable list:', mutable_list)
