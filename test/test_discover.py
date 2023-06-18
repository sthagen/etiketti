from etiketti.discover import get_producer


def test_get_producer():
    label = get_producer()
    assert label.startswith('lltx-1.')
    assert 'txlv-202' in get_producer()
