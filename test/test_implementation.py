import etiketti.implementation as impl


def test_camelize_first_two():
    assert impl.camelize_first_two('a-b-c-d') == 'AB'
