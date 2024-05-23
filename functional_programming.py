# Functional progrramming indeed

# Hint: определяем базовый случай и стараемся все свести к нему.
# Базовый случай для массивов часто оказывается пустой массив или массив из одного элемента.
# Если не знаешь с чего начать - начни с этого.

def array_sum(arr):
    """
    :param arr: array of number
    :return: numbers sum of array
    """
    if arr == []:
        return 0
    return arr[0] + array_sum(arr[1:])

print(array_sum([1, 2, 3]))



