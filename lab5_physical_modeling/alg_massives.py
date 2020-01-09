def square_massive(A):  # возведение всех элементов массива в квадрат
    """
    This function will sqare every elemet of the given massive.

    """
    for k in range(5):
        A[k] *= A[k]
    print(A)


def fulfill_massive():  # массив в обратном порядке
    """
    Создание пустого массива из целых чисел.
    Его заполнение числами с клаватуры, до тех пор пока не введен '0'.
    Вывод введенного массива чисел в обратном порядке.
    'top' - подсчет введенных элементов массива отличных от нуля
    """
    A = [0] * 1000
    print('Введите элементы массива:')
    x = int(input())
    top = 0
    while x != 0:
        A[top] = x
        top += 1
        x = int(input())
    print('Количество введенных элементов:', top)
    print('Введенный массив в обратном порядке:')
    for k in range(top - 1, -1, -1):
        print(A[k])


def copy_massive():  # копирование элементов массива А в массив В
    """"
    С клавиатуры вводится массив 'A' размера 'N' и он копируется в массив 'B'.
    Массив 'B' сохраняется в памяти.
    Последующие операции с массивом 'A' не приведут к изменению в массиве 'B'.
    """
    print('Введите число элементов массива:')
    N = int(input())
    A = [0] * N
    B = [0] * N
    print('Введите элементы массива:')
    for k in range(N):
        A[k] = int(input())
    for k in range(N):
        B[k] = A[k]

    print('Исходный массив:', A)
    print('Скопированный массив:', B)


def array_search(A: list, N: int, x: int):  # поиск заданного числа в массиве
    """
    Осуществляет поиск числа x в массиве 'A'
    от 0 до N-1 индекса включительно.
    Возвращает индекс элемента x в массиве A.
    Или '-1', если такого нет.
    Если в массиве несколько элементов равных x то вернуть индекс первого.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def inver_array(A, N):  # поворот массива задои - наперед
    """
    Обращение массива (поворот задом наперед)
    в рамках индексов от 0 до N-1
    """
    for k in range(N // 2):
        A[k], A[N - k - 1] = A[N - k - 1], A[k]


def cycle_move_right(A, N):  # циклический сдвиг вправ
    """
    Задается массив A состоящий из N элементов.
    Массив сдвигается на 1 элемент вправо.
    Последний элемент становится первым.
    Пример:
    Ввод: [0, 1, 2, 3, 4, 5]
    Вывод: [5, 0, 1, 2, 3, 4]
    """
    tmp = A[N - 1]
    for k in range(N - 2, -1, -1):
        A[k + 1] = A[k]
    A[0] = tmp


def cycle_move_left(A, N):  # циклический сдвиг вправо
    """
    Задается массив A состоящий из N элементов.
    Массив сдвигается на 1 элемент влево.
    Первый элемент становится последним

    Пример:
    Ввод: [0, 1, 2, 3, 4, 5]
    Вывод: [1, 2, 3, 4, 5, 0]
    """
    tmp = A[0]
    for k in range(N - 1):
        A[k] = A[k + 1]
    A[N - 1] = tmp


def eratosthenes_sieve(N):
    """
    Решения задачи поиска всех простых чисел в последовательном массиве до N.
    Пример:
    Ввод: 15
    Вывод: 3, 5, 7, 11, 13
    """
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2 * k, N, k):
                A[m] = False
    print(A)
    for k in range(N):
        print(k, '-', 'простое' if A[k] else 'составное')


def test_cycle_move_left():
    A1 = [0, 1, 2, 3, 4, 5]
    print('before:', A1)
    cycle_move_left(A1, 6)
    print('after:', A1)
    if A1 == [1, 2, 3, 4, 5, 0]:
        print('test1 - ok')
    else:
        print('test1 - fail')

    A2 = [312, 3134, 544, 34, -232, -54, -35]
    print('before:', A2)
    cycle_move_left(A2, 7)
    print('after:', A2)
    if A2 == [3134, 544, 34, -232, -54, -35, 312]:
        print('test2 - ok')
    else:
        print('test2 - fail')

    A3 = [3, 4, 5, 6, -2, -5]
    print('before:', A3)
    cycle_move_left(A3, 6)
    print('after:', A3)
    if A3 == [4, 5, 6, -2, -5, 3]:
        print('test3 - ok')
    else:
        print('test3 - fail')


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print('test1 - ok')
    else:
        print('test1 - fail')

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print('test2 - ok')
    else:
        print('test2 - fail')

    A3 = [10, 20, 30, 40, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print('test3 - ok')
    else:
        print('test3 - fail')


def test_cycle_move_right():
    A1 = [0, 1, 2, 3, 4, 5]
    print('before:', A1)
    cycle_move_right(A1, 6)
    print('after:', A1)
    if A1 == [5, 0, 1, 2, 3, 4]:
        print('test1 - ok')
    else:
        print('test1 - fail')

    A2 = [7, 8, 9, 10, 423, 345, 525, 499]
    print('before:', A2)
    cycle_move_right(A2, 8)
    print('after:', A2)
    if A2 == [499, 7, 8, 9, 10, 423, 345, 525]:
        print('test2 - ok')
    else:
        print('test2 - fail')

    A3 = [-1, -23, -9, -21, -223, 45, 25, 1499]
    print('before:', A3)
    cycle_move_right(A3, 8)
    print('after:', A3)
    if A3 == [1499, -1, -23, -9, -21, -223, 45, 25]:
        print('test3 - ok')
    else:
        print('test3 - fail')


def test_invert_array():
    # test1
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    inver_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print('test1 - ok')
    else:
        print('test1 - fail')
    # test2
    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    inver_array(A2, 8)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('test2 - ok')
    else:
        print('test2 - fail')


eratosthenes_sieve(1000)
