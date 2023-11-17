from pytest import raises
from testing.basic import parser

def test_basic():
    assert parser('abc') == ['abc']
    assert parser('a,b,c') == ['a', 'b', 'c']
    assert parser('a|b|c', delimiter='|') == ['a', 'b', 'c']
    assert parser('a,b,c', transform=lambda val: val+val) == ['aa', 'bb', 'cc']

    with raises(TypeError, match="'bool' object is not callable"):
        parser('a,b,c', transform=False)

    with raises(AttributeError, match="'int' object has no attribute 'split'"):
        parser(123)


