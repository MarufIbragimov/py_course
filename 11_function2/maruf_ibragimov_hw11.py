def find_min_max(numbers: list[float]) -> tuple[float, float]:
    """
    Принимает список чисел и возвращает кортеж 
    из минимального и максимального значений.
    """
    min_value = numbers[0]
    max_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value


def squares_dict(n: int) -> dict:
    """
    Принимает число n и возвращает словарь, 
    где ключи — числа от 1 до n, а значения — их квадраты.
    """
    squares = {}

    for num in range(1, n + 1):
        squares[num] = num ** 2

    return squares


def shift_list(lst: list, k: int) -> list:
    """
    принимает список и число k и возвращает новый список, 
    сдвинутый вправо на k позиций
    """
    shifted = []
    lst_length = len(lst)

    for i, x in enumerate(lst):
        i_shift = i + k

        if i_shift < lst_length:
            shifted.insert(i_shift, x)
        else:
            shifted.insert(i_shift - lst_length, x)

    return shifted