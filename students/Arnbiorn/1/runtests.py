import glob # noqa: E902,E261
import os
import imp

extension = '.py'
prefix = 'test_'


def search(directory, pattern):
    """filepath list"""
    return glob.glob('{0}/{1}'.format(directory, pattern), recursive=True)


def module_loading(file):
    """return imported modules or none"""
    name = os.path.basename(file).replace(extension, '')

    if len(name) == 0 or (not os.path.exists(file)):
        return None

    modules = imp.load_source(name, file)
    return modules


def find_test(module):
    """return funcDict or none"""
    global prefix
    if module is None:
        return None
    return dict(filter(lambda obj: obj[0].startswith(prefix), vars(module).items()))  # noqa: E501


def validating_test(function):
    """check test_function"""
    try:
        function
    except AssertionError:
        return 'Fail'
    return 'Ok'


def testing(directorys=''):
    """find test in dict, and check them"""
    if not directorys:
        directorys = os.getcwd()

    for files in search(directorys, '{0}*{1}'.format(prefix, extension)):
        module = module_loading(files)
        if module is None:
            continue
        for tests in validating_test(module):
            print('{0}-{1}'.format(
                files,
                validating_test(tests[0]),
            ))  # noqa: T001
