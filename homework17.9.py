numbers = input("Введите список чисел через пробел: ")
number = int(input("Введите любое число: "))

# Проверяем корректно-ли введены данные.
try:
    if "," in numbers:
        raise ValueError
except ValueError:
    print("Ошибка при вводе данных. Попробуйте снова.")
    raise

# Преобразовываем строку в список чисел.
numbers = list(map(int, numbers.split()))

# Сортируем
for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Проверяем что бы введенное число не выходило за пределы списка.
try:
    if number > numbers[-1]:
        raise IndexError
except IndexError:
    print("Введенное вами число больше максимального числа указанного в списке, попробуйте снова.")
    raise

# Выводим на экран отсортированный список и его тип.
print("Отсортированный список чисел: ", numbers)
print("И его тип:", type(numbers))
print()

# Бинарный алгоритм поиска
def binary_search(array, element, left, right):
    if left > right:
        print("Введенное вами число отсутствует в списке.")
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


# Проверяем что бы введенное число не было последним в списке.
try:
    numpos = (binary_search(numbers, number, 0, len(numbers)))
    if numbers[numpos] == numbers[-1]:
        print("Введенное вами число - последнее в списке.")
        raise IndexError
    if numbers[numpos] == numbers[0]:
        print("Введенное вами число - первое в списке.")
        raise IndexError
except IndexError:
    print("Введенное вами число не соответствует условиям, попробуйте снова.")
    raise


# Находим числа слева и справа от указанного.
num1 = (binary_search(numbers, numbers[numpos-1], 0, len(numbers)))
num2 = (binary_search(numbers, numbers[numpos+1], 0, len(numbers)))

# Если все введено корректно, то мы получаем номера позиций чисел.
if numbers[num1] != numbers[num1-1]:
    print("Номер номер позиции элемента, который меньше введенного вами числа: ", num1,
    "\nЧисло равно: ", numbers[num1])
    print("Номер номер позиции элемента, который больше или равен введенному вами числу: ", num2,
    "\nЧисло равно: ", numbers[num2])

# Данная конструкция нужна если указанное нами число повторяется в списке несколько раз,
# она идет по списку пока не найдет число, идущее до него.
else:
    for i in numbers:
        while numbers[num1] == numbers[num1-1]:
            num1 = num1-1
    print("Номер номер позиции числа, которое меньше введенного вами числа: ", num1-1,
          "\nЧисло равно: ", numbers[num1-1])
    print("Номер номер позиции числа, которое больше или равно введенному вами числу: ", num1+1,
          "\nЧисло равно: ", numbers[num1+1])
