# -*- coding: utf-8 -*-

import glob # noqa: E902,E261
import imp
import os

extension = '.py'
prefix = 'test_'


def search(directory, pattern):
    """Filepath list."""
    return glob.glob('{0}/{1}'.format(directory, pattern), recursive=True)


def module_loading(file):  # noqa: WPS110
    """Return imported modules or none."""
    file_name = os.path.basename(file).replace(extension, '')

    if (not file_name) or (not os.path.exists(file)):
        return None

    modules = imp.load_source(file_name, file)
    return modules  # noqa: WPS331


def find_test(module):
    """Return funcDict or none."""
    if module is None:
        return None
    return dict(filter(lambda obj: obj[0].startswith(prefix), vars(module).items()))  # noqa: E501, WPS221, WPS110


def validating_test(function):
    """Check test_function."""
    try:
        function()
    except AssertionError:
        return 'Fail'
    return 'Ok'


def testing(directorys=''):
    """Find test in dict, and check them."""
    if not directorys:
        directorys = os.getcwd()

    for files in search(directorys, '{0}*{1}'.format(prefix, extension)):
        module = module_loading(files)
        if module is None:
            continue
        for tests in validating_test(module):
            print('{0}-{1}'.format(  # noqa: T001
                files,
                validating_test(tests[0]),
            ))
