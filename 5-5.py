def calculate_average(number_list):
    try:
        if type(number_list) is not list:
            raise ValueError("You should pass list to this function!")
    except ValueError as err:
        print(err)
        return
    try:
        average = sum(number_list) / len(number_list)
    except TypeError:
        print("List should contain numbers!")
        return
    return average

print(calculate_average([1, 2, 3]))
print(calculate_average(1))
print(calculate_average(["a", 1]))
