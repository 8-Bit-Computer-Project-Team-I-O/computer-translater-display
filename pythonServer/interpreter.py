def get_clock(values):
    return values[0]


def get_bus(values):
    return values[1]


def get_mc(values):
    return values[2]


# DO INTERPRETATION IN HERE
def interpret(vals_array):
    print(get_clock(vals_array))
    if get_clock(vals_array) == "0":
        print("Epoch passed")
