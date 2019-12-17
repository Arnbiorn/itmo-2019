import glob # noqa: E902,E261
import os
import imp

extension = '.py'
prefix = 'test_'


 def search(directory, pattern):  # noqa: E113,E111, E303
    return glob.glob('{0}/{1}'.format(directory, pattern), recursive=True)


 def module_loading(file):  # noqa: E113,E111, E303
    name = os.path.basename(file).replace(extension, '')

    if len(name) == 0 or (not os.path.exists(file)):
        return None

    modules = imp.load_source(name, file)
    return modules


 def find_test(module):  # noqa: E113,E111, E303
    global prefix
    if module is None:
        return None
    return dict(filter(lambda obj: obj[0].startswith(prefix), vars(module).items()))


 def testing(directorys=''):  # noqa: E113,E111, E303
    if len(directorys) == 0:
        directorys = os.getcwd()

     for files in search(directorys, '{0}*{1}'.format(prefix, extension)):
        module = module_loading(files)

         if module is None:
            continue

         for tests in find_test(module)items():
            try:
                tests[1]()
                result = 'ok'
            except AssertionError:
                result = 'fail'

             print('{0}-{1}-{2}'.format(
                 name,
                 test[0],
                 result
             ))


 if __name__ == '__main__':
    testing(input("Write directory path(or press Enter to work in this dir): "))
