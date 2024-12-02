def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        for i in range(2, 3, 5):
            if result % i == 0 and result / i != 1:
                print("Составное")
                break
            else:
                print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


############
result = sum_three( 2, 3,  6)
print(result)
