text = input()


def uppercase_decorator(func):
    def wrapper(te):
        return func(text).upper()
    return wrapper


@uppercase_decorator
def display_text(text):
    return text


print(display_text(text))
