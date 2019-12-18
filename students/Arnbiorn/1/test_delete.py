def filter_empty(sequence):
    return list(filter(
        lambda string: len(string),
        sequence
    ))


def test_delete():
    assert filter_empty([]) == []
    assert filter_empty(['']) == []
    assert filter_empty(['', '']) == []
    assert filter_empty(['a', '']) == ['a']
    assert filter_empty(['a', 'b']) == ['a', 'b']


if __name__ == '__main__':
    test_delete()
