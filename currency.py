def convert(rates, value, from_string, to_string):
    """Takes a list of rates, and takes an amount of currency(value),
    and """
    tuple_list = [x for x in rates if x[0]==from_string and x[1]==to_string]
    return tuple_list[0][2] * value




if __name__ == "__main__":
    pass

rates = [("USD", "EUR", 0.74)]
print(convert(rates, 1, "USD", "EUR"))
