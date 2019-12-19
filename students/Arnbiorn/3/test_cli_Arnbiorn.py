# -*- coding: utf-8 -*-

import subprocess

from cli import contains, ls, mk, rm, since


def test_ls(ls_fixture):
    """ls test function."""
    dirrectory, result_count = ls_fixture
    assert len(ls(dirrectory)) == result_count


def test_mk(tmp_path, mk_fixture):
    """mk test function."""
    filename, result, add_path = mk_fixture
    path = tmp_path / filename if add_path else filename
    assert mk(path) == result


def test_rm(rm_fixture):
    """rm test function."""
    path, result = rm_fixture
    assert rm(path) == result


def test_contains(contains_fixture):
    """contains test function"""
    path, result = contains_fixture
    assert contains(path) == result


def test_since(since_fixture):
    """since test function."""
    dirrectory, argument, result = since_fixture
    assert since(argument, dirrectory) == result


def test_integration(integration_fixture):
    """integration test function."""
    command, arg = integration_fixture
    format_str = 'python students/Arnbiorn/3/cli.py {0}'  # noqa E800
    command_str = format_str.format(command)
    assert subprocess.call(command_str, shell=True) == 0  # noqa: S602
