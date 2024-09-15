immutable_var = (5, 1.5, 'text')
print(immutable_var)
# immutable_var[0] = 3
# При попытке замены данных в кортеже, выпадает ошибка:
# TypeError: 'tuple' object does not support item assignment
# связанно это с тем что особенностью кортежа является неизменяемость данных.
mutable_list = [1.2, 13, 'string']
mutable_list[0] = int(mutable_list[0])
print(mutable_list)
