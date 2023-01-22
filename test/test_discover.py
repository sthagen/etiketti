from etiketti.discover import get_producer


def test_get_producer():
    assert get_producer().startswith('lltx-1.15.0-txlv-2022-')
