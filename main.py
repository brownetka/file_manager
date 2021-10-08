import sys
import basic_funcs

help_msg = """
        Welcome in the console`s file manager!
        Available commands:
        1.  help - to see this message again
        2.  delete - to delete file or directory
        3.  whereami - too see path where you are
        4.  copy - to copy file or directory
        5.  move - to move file or directory
        6.  rename - to rename file or directory
        7.  write - to write something in a file
        8.  list_files - to give a list of files
        9.  list_dirs - to give a list of directories
        10.  create_file - to create a new file
        11. create_folder - to create a new folder
        12. change_directory - if you want to move between directories
        13. exit - to exit from the file manager
    """
work_directory = sys.argv[0].lstrip('/').split(sep='/')[:-1]
work_directory[0] = '/' + work_directory[0]
work_path = '/'.join(work_directory) + '/'

print(help_msg)
while True:
    cmd = input('Enter a command\n')
    if cmd == 'help':
        print(help_msg)

    elif cmd == 'exit':
        exit(print('Thank you! Bye!'))

    elif cmd == 'whereami':
        print('/'.join(work_directory), end='\n\n')

    elif cmd == 'delete':
        delete_file_name = input('Enter a name of file that you want to delete\n')
        basic_funcs.delete_file(work_path + delete_file_name)

    elif cmd == 'copy':
        name = input('Enter a name of file or directory that you want to copy\n')
        if name.startswith('/') and not basic_funcs.check_bounds('/'.join(work_directory), name):
            print('Error! You can`t choose this directory!')
            continue
        new_name = input('Enter a name of new file. Also you can type there a full path\n')
        if '/' not in new_name:
            new_name = work_path + new_name
        basic_funcs.copy_file(name, new_name)

    elif cmd == 'move':
        name = input('Enter a name of file or directory that you want to move\n')
        if name.startswith('/') and not basic_funcs.check_bounds('/'.join(work_directory), name):
            print('Error! You can`t choose this directory!')
            continue
        new_name = input('Enter a directory to move or also yo can type a full path\n')
        if '/' not in new_name:
            new_name = work_path + new_name
        basic_funcs.move_or_rename_file(name, new_name)

    elif cmd == 'rename':
        name = input('Enter a name of file or directory that you want to rename\n')
        if name.startswith('/') and not basic_funcs.check_bounds('/'.join(work_directory), name):
            print('Error! You can`t choose this directory!')
            continue
        new_name = input('Enter a new name\n')
        basic_funcs.move_or_rename_file(name, new_name)

    elif cmd == 'write':
        name = input('Enter a name of file or directory that you want to write in\n')
        if name.startswith('/') and not basic_funcs.check_bounds('/'.join(work_directory), name):
            print('Error! You can`t choose this directory!')
            continue
        text = input('What text do you want to write there?\n')

        if '/' not in name:
            name = work_path + name
        basic_funcs.add_text_to_file(name, text)

    elif cmd == 'list_files':
        basic_funcs.get_list(work_path)

    elif cmd == 'list_dirs':
        basic_funcs.get_list(work_path, folders_only=True)

    elif cmd == 'create_file':
        name = input('Enter a name for a new file\nAlso you can type a full path of file (with name)\n')
        if name.startswith('/') and not basic_funcs.check_bounds('/'.join(work_directory), name):
            print('Error! You can`t choose this directory!')
            continue
        text = input('Enter some text if you want to put it inside. Or just press ENTER\n')
        if '/' not in name:
            name = work_path + name
        basic_funcs.create_file(name, text=text)

    elif cmd == 'change_directory':
        print("""
        . if you want to stay in current directory
        .. if you want to step up
        <folder name> if you want to step down into current folder
        """)
        folder = input()
        work_directory = basic_funcs.cd_command(work_directory, folder)
        work_path = '/'.join(work_directory) + '/'
    elif cmd == 'create_folder':
        name = input('Enter a name for a new folder\nAlso you can type a full path\n')
        if name.startswith('/') and not basic_funcs.check_bounds('/'.join(work_directory), name):
            print('Error! You can`t choose this directory!')
            continue
        if '/' not in name:
            name = work_path + name
        basic_funcs.create_folder(name)
    else:
        print('Wrong command. Bye!')
