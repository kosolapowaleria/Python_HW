def is_year_leap(year):
    return True if 0 == year % 4 == 0 else False

year_check = int(input('Введите год: '))
result = is_year_leap(year_check)
print(f'год {year_check}: {result}')