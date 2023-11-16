def main():
    x, y = get_fraction("Fraction: ")
    percentage = round(x / y * 100)

    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


def get_fraction(message):
    while True:
        user_input = input(message)
        if "/" in user_input:
            try:
                x, y = user_input.split("/")
                x = int(x)
                y = int(y)
            except ValueError:
                pass
            else:
                if x <= y and y > 0:
                    return x, y


main()
