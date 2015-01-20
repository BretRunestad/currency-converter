from currency import*

def test_convert_value_check():
    assert convert(rates= [('USD', 'USD', 1)],
                   value = 5,
                   from_string = 'USD',
                   to_string = 'USD') == 5

def test_convert_dollar_to_euro():
    rates = [('USD', 'EUR', .74), ('USD', 'JPY', 145.949)]
    assert convert(rates,
                   value = 1,
                   from_string = 'USD',
                   to_string = 'EUR') == 0.74

def test_convert_different_values():
    rates = [('USD', 'EUR', .74), ('USD', 'JPY', 145.949)]
    assert convert(rates, value = 5,
                   from_string = 'USD', to_string ='EUR') == 3.7
    assert convert(rates, value = .2,
                   from_string = 'USD', to_string = 'EUR') == 0.15
    assert convert(rates, value = 0,
                   from_string = 'USD', to_string = 'EUR') == 0

def test_flipped_conversion():
    rates = [('USD', 'EUR', .74), ('USD', 'JPY', 145.949)]
    assert convert(rates, value = 1,
                   from_string = 'EUR', to_string = 'USD') == 1.35

def test_multiple_conversions():
    rates = [('USD', 'EUR', .74),
             ('USD', 'JPY', 145.949),
             ('USD', 'CAD', 1.21)]
    assert convert(rates, value = 500,
                   from_string = 'USD', to_string = 'EUR') == 370
    assert convert(rates, value = 500,
                   from_string = 'EUR', to_string = 'USD') == 675.68
    assert convert(rates, value = 500,
                   from_string = 'USD', to_string = 'JPY') == 72974.5
    assert convert(rates, value = 500,
                   from_string = 'JPY', to_string = 'USD') == 3.43
    assert convert(rates, value = 500,
                   from_string = 'USD', to_string = 'CAD') == 605
