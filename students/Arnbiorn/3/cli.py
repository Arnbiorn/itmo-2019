# -*- coding: utf-8 -*-

import argparse  # noqa: I001
import os
import sys
unknwn_command = 'Error! Unknown command!'  # noqa: I003


def main(commands, module):
    """Main."""
    performed = commands[0]
    command_list = {
        'ls': ls,
        'mk': mk,
        'rm': rm,
        'contains': contains,
        'since': since,
    }
    if performed in command_list:
        function = command_list[performed]
        argument = commands[1] if len(commands) > 1 else None
        function(argument)
    else:
        print('Error! Unknown command!')  # noqa T001


def ls(argument=None):
    """ls."""
    directory = os.getcwd() if argument is None else argument
    result = os.scandir(directory)  # noqa: WPS110
    filtered = filter(lambda zxc: zxc.is_file(), result)
    mapped = list(map(lambda zxc: zxc.name, filtered))
    dirs = [folder.name for folder in os.scandir(directory) if folder.is_dir()]
    return mapped + dirs


def mk(argument=None):
    """mk."""
    if not argument:
        return unknwn_command
    if os.path.exists(argument):
        return 'FILE_EXISTS'
    try:
        open(argument, 'a').close()  # noqa WPS515
    except OSError:
        return 'ERROR! UNKNOWN FILENAME'
    return 'Ok'


def rm(argument=None):
    """rm."""
    if not argument:
        return 'Error! Unknown command!'
    if os.path.isdir(argument):
        return 'ARGUMENT_IS_DIR'
    if not os.path.exists(argument):
        return 'NOT_FOUND'
    os.remove(argument)
    return 'Ok'


def contains(argument=None):
    """contains."""
    if not argument:
        return unknwn_command
    if os.path.isdir(argument):
        return 'ARGUMENT_IS_DIR'
    result_list = ls()
    if argument in result_list:
        return 0
    return 1


def since(timestamp, directory=os.getcwd()):  # noqa WPS404, B008
    """since."""
    try:
        timestamp = int(timestamp)
    except Exception:
        return unknwn_command
    if not directory:
        return unknwn_command
    if not os.path.exists(directory):
        return 'DIRECTORY_NOT_FOUND'
    if not ls(directory):
        return 'DIRECTORY_IS_EMPTY'
    result_list = []
    for path in ls(directory):
        format_str = '{0}/{1}'
        formatted = format_str.format(directory, path)
        creation_time = os.stat(formatted).st_ctime
        if creation_time > timestamp:
            result_list.append(path)
    return result_list


def make_parser():
    """Argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, nargs='*', help='Action')
    return parser


if __name__ == '__main__':
    arguments = make_parser().parse_args()
    current_module = sys.modules[__name__]
    main(arguments.action, current_module)
