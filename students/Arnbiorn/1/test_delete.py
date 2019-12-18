def filter_empty(sequence):
    """Just function"""
    return list(filter(
        lambda string: len(string),
        sequence,
    ))


def test_delete():
    """Just test_function"""
    assert filter_empty([]) == []  # noqa: WPS520
    assert filter_empty(['']) == []  # noqa: WPS520
    assert filter_empty(['', '']) == []  # noqa: WPS520
    assert filter_empty(['a', '']) == ['a']
    assert filter_empty(['a', 'b']) == ['a', 'b']


if __name__ == '__main__':
    test_delete()
