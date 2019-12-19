import datetime

import pytest
import os  # noqa I001
import shutil  # noqa I001

empty_string = ''
file = 'file.txt'  # noqa: WPS110
point = '.'
dirrectory = 'dir'
error = 'ERROR! Wrong argument!'


@pytest.fixture()
def timestamps():
    """Timestamps."""
    return int(datetime.datetime.timestamp(datetime.datetime.now())) - 10


@pytest.fixture(params=[
    ('empty', [], 0),
    ('directory', [dirrectory], 1),
    ('files', [file], 1),
    ('dirrectory_and_file', [dirrectory, file], 2),
])
def ls_fixture(tmp_path, request):
    """Ls fixture."""
    work_dirrectory = tmp_path / request.param[0]
    paths, result_count = request.param[1], request.param[2]
    work_dirrectory.mkdir()
    for path in paths:
        objects = work_dirrectory / path  # noqa: WPS110
        if point in path:
            objects.write_text(empty_string)
        else:
            objects.mkdir()
    yield (work_dirrectory, result_count)


@pytest.fixture(params=[
    (empty_string, error, False),
    (file, 'Ok', True),
    ('file.txt', 'Ok', True),
    ('f/1/l/e.txt', 'ERROR! UNKNOWN FILENAME', True),
    ('students/Arnbiorn/3/cli.py', 'FILE_EXISTS', False),
])
def mk_fixture(tmp_path, request):
    """Mk fixture."""
    yield request.param


@pytest.fixture(params=[
    (dirrectory, 'ARG_IS_DIR', True),
    (file, 'FILE_NOT_FOUND', False),
    (empty_string, error, 'False'),
    (file, 'Ok', True),
])
def rm_fixture(tmp_path, request):
    """Rm fixture."""
    path, expected_result, should_create = request.param
    final_path = path
    is_file = point in final_path
    if final_path and should_create:
        final_path = tmp_path / path
        final_path.write_text(empty_string) if is_file else final_path.mkdir()  # noqa WPS428
    yield (final_path, expected_result)


@pytest.fixture(params=[
    (empty_string, error, False),
    (file, 0, True),
    (dirrectory, 'ARG_IS_DIR', True),
    (file, 1, False),
])
def contains_fixture(request):
    """Contains."""
    path, expected_result, should_create = request.param
    is_file = point in path
    if path and should_create:
        if is_file and not os.path.exists(path):
            open(path, 'a').close()  # noqa WPS515
        else:
            os.mkdir(path)
    yield (path, expected_result)
    if should_create:
        shutil.rmtree(path) if not is_file else os.remove(path)  # noqa WPS441, WPS428


@pytest.fixture(params=[  # noqa C901
    ([None], error, False),
    ([dirrectory], 'DIR_NOT_FOUND', False),
    ([dirrectory], 'DIR_IS_EMPTY', True),
    (['dir/another dir'], ['another dir'], True),
    (['dir/file.txt'], [file], True),
    (['dir/subdir', 'dir/file.txt'], [file, 'subdir'], True),
])
def since_fixture(request, timestamps):  # noqa WPS442
    """Since."""
    paths, expected_result, should_create = request.param
    work_dirrectory = paths[0]
    if work_dirrectory and should_create:
        if '/' in work_dirrectory:
            work_dirrectory = work_dirrectory.split('/')[0]
        os.mkdir(work_dirrectory)
    if should_create:
        for path in paths:
            if path and not os.path.exists(path):
                is_file = point in path
                if is_file:
                    open(path, 'a').close()  # noqa WPS515
                else:
                    os.mkdir(path)
    yield (work_dirrectory, timestamps, expected_result)
    if should_create:
        for another_path in paths:  # noqa WPS440
            if another_path:
                if point in another_path:
                    os.remove(another_path)
                else:
                    shutil.rmtree(another_path)
    if work_dirrectory and os.path.exists(work_dirrectory):
        shutil.rmtree(work_dirrectory)


@pytest.fixture(params=[
    ('ls', empty_string),
    ('mk', file),
    ('contains', file),
    ('since', timestamps),
    ('rm', file),
])
def integration_fixture(request):
    """Fixture."""
    yield request.param
