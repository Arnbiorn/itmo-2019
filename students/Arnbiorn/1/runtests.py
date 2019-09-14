import glob
import os
import imp

file_ext = '.py'
file_pref = 'test_'

def file_search(directory, pattern):
    return glob.glob(f"{directory}/{pattern}", recursive=True)

def module_load(file):
    global file_ext
    name = os.path.basename(file).replace(file_ext, '')

    if len(name) == 0 or (not os.path.exists(file)):
        return None

    modules = imp.load_source(name, file)
    return modules

def find_test(mod):
    global file_pref
    if mod is None:
        return None
    return dict(filter(lambda obj: obj[0].startswith(file_pref), vars(mod).items()))

def testing(directorys=''):
    if len(directorys) == 0:
        directorys = os.getcwd()

    files_with_test = file_search(directorys, f"*{file_ext}")

    for files in files_with_test:
        mod = module_load(files)

        if mod is None:
            continue

        test = find_test(mod)

        for tests in test.items():
            try:
                tests[1]()
                result = 'ok'
            except AssertionError:
                result = 'fail'

            print(f"{files_with_test} - {tests[0]} - {result}")

if __name__ == '__main__':
    testing(input("Write directory path(or press Enter to work in this dir): "))
