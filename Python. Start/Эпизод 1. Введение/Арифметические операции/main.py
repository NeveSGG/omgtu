# при делении всегда получается float
price = 50
discont_coeff = 2
result = price / discont_coeff
print(result)
print(type(result))

# получения целой части от деления
result = price // 3
print(result)

# остаток от деления
result = 3 % 2
print(result)

# Логические операции
print(price > discont_coeff)

# Сложные логические операции
print(1 > 2 and 4 > 3)
print(1 > 2 or 4 > 3)
print(not (1 > 2 or 4 > 3))
