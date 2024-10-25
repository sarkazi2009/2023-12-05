def sum_three(a, b, c):
    return a + b + c


def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result > 1:
            if all(result % i for i in range(2, int(result ** 0.5) + 1)):
                print("Простое")
            else:
                print("Составное")
        else:
            print("Не является числом")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
