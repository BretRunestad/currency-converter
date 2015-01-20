def convert(rates, value, from_string, to_string):
    """Takes a list of rates, an amount of currency(value), a from_string, and
    a to_string.  It cross references the 'from' and 'to' strings to find the
    applicable currency exchange rate.  It then multiplies the value by that
    rate, rounded to 2 decimal places."""
    tuple_list = [x for x in rates if x[0]==from_string and x[1]==to_string]
    if tuple_list:
        return round(tuple_list[0][2] * value, 2)
    else:
        tuple_list2 = [x for x in rates if x[1]==from_string and x[0]==to_string]
        return round((1/tuple_list2[0][2]) * value, 2)




if __name__ == "__main__":
    pass

rates = [("USD", "EUR", 0.74)]
print(convert(rates, 1, "USD", "EUR"))
