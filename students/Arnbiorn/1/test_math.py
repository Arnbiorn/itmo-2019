# -*- coding: utf-8 -*-


def my_sum(first, secound):
    """Just sum function."""
    return first + secound


def my_mult(first, secound):
    """Just mult function."""
    return first * secound


def test_sum():
    """Just test_sum_function."""
    assert my_sum(1, 2) == 3
    assert round(my_sum(2.1, 4.2), 2) == 6.3  # noqa: WPS432


def test_mult():
    """Just test_mult_function."""
    assert my_mult(-6, -4) == 24
