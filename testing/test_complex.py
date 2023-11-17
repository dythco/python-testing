from pytest import raises
from testing.complex import complex, complex_1, complex_2

def test_complex():
    assert complex('a,b,c') == ['aa', 'bb', 'cc']

def test_complex_1():
    assert complex_1('a|1|2|3,b|4|5|6,c|7|8|9') == [['aa', 1, 2, 3], ['bb', 4, 5, 6], ['cc', 7, 8, 9]]

def test_complex_2():
    assert complex_2('a|1|2|3,b|4|5|6,c|7|8|9') == [['aa', 1, 2, 3], ['bb', 4, 5, 6], ['cc', 7, 8, 9]]