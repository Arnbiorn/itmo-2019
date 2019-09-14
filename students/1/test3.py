from datetime import datetime

def is_adult(
    input_function=input,
    today_function=datetime.now,
):
    users_birthday = datetime.strptime(
        input_function('Your birstday:'),
        '%Y.%m.%d',
    )
    delta = today_function() - users_birthday
    return delta.days / 365 >= 18


def test_is_adult():
    assert is_adult(
        lambda _: '1905.04.01',
        lambda: datetime(year=2019, month=9, day=1),
    )
    assert is_adult(
        lambda _: '2018.04.01',
        lambda: datetime(year=2019, month=9, day=1),
    ) is False

if __name__ == '__main__':
    test_is_adult()
    