class User:
    def __init__(self):
        is_authenticated = True

def decorator(func):
    def decorated(x, y):
        if x >= 0 and y >= 0:
            return func(x, y)
        return 'error'

    return decorated

@decorator
def exp(x, y):
    print("square = ", x * y)
    print("tri = ", x * y / 2)

exp(2, 4)