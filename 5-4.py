def distance_between_dots(x1, y1, x2, y2):
    try:
        coordinates = [x1, y1, x2, y2]
        for c in coordinates:
            if type(c) is not int and type(c) is not float:
                raise ValueError
    except ValueError:
        print("Arguments are not numbers!")
        return
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return distance

print(distance_between_dots(1, 1, 2, 2))
print(distance_between_dots("a", 1, 2, 3))
