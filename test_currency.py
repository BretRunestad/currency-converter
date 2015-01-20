from currency import*

def test_convert_value_check():
    assert convert(rates= [('USD', 'USD', 1)],
                   value = 5,
                   from_string = 'USD',
                   to_string = 'USD') == 5

def test_convert_dollar_to_euro():
    rates = [('USD', 'EUR', .74), ('USD', 'JPY', 1.2)]
    assert convert(rates = [('USD', 'EUR', .74)],
                   value = 1,
                   from_string = 'USD',
                   to_string = 'EUR') == 0.74
