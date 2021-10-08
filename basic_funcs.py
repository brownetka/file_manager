import os
import shutil
import sys


def create_file(name, text=None):
    with open(name, 'w', encoding='utf8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Error! Folder with this name is existed')


def get_list(working_directory, folders_only=False):
    result = os.listdir(working_directory)
    if folders_only:
        result = list(filter(lambda x: True if os.path.isdir(x) else False, result))
    print(result)


def delete_file(name):
    try:
        if os.path.isdir(name):
            try:
                os.rmdir(name)
            except OSError:
                print("Directory is not empty.\nAre you sure?\nType YES for delete\nOr something to cancel")
                if input() == "YES":
                    shutil.rmtree(name)
                    print('Directory has been deleted')
                else:
                    print('Directory has not been deleted')
        else:
            os.remove(name)
    except FileNotFoundError:
        print("Error! This file doesn't exist!")


def copy_file(name, new_name):
    try:
        if os.path.isdir(name):
            try:
                shutil.copytree(name, new_name)
            except FileExistsError:
                print('Error! Folder with this name is existed')
        else:
            shutil.copy(name, new_name)
    except FileNotFoundError:
        print("This file doesn't exist!")


def add_text_to_file(name, text):
    with open(name, mode='a', encoding='utf8') as f:
        f.write(text)


def move_or_rename_file(name, path):
    try:
        shutil.move(name, path)
    except FileNotFoundError:
        print('Error! File not found!')


def cd_command(work_directory, cmd):
    if cmd == '.':
        return work_directory
    elif cmd == '..':
        return work_directory[:-1]
    else:
        if os.path.isdir(cmd):
            return work_directory + [cmd]


def check_bounds(work_path, new_path):
    if new_path.startswith(work_path):
        return True
    else:
        return False


