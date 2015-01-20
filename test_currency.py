from currency import*

def test_convert_value_check():
    assert convert(rates=.75,
                   value = 5,
                   from_string = 'USD',
                   to_string = 'USD') == 5
