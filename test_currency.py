from currency import*

def test_convert_value_check():
    assert convert(rates= [('USD', 'USD', 1)],
                   value = 5,
                   from_string = 'USD',
                   to_string = 'USD') == 5

def test_convert_dollar_to_euro():
    rates = [('USD', 'EUR', .74), ('USD', 'JPY', 1.2)]
    assert convert(rates,
                   value = 1,
                   from_string = 'USD',
                   to_string = 'EUR') == 0.74

def xtest_convert_different_values():
    rates = [('USD', 'EUR', .74), ('USD', 'JPY', 1.2)]
    assert convert(rates, value = 5,
                   from_string = 'USD', to_string ='EUR') == 3.7
    assert convert(rates, value = .2,
                   from_string = 'USD', to_string = 'EUR') == 0.148
    assert convert(rates, value = 0,
                   from_string = 'USD', to_string = 'EUR') == 0
