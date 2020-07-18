import re
import sys
import os
import subprocess


def rename(m):
    main_num = m.group(1)
    sub_num = m.group(2)
    text = m.group(3)
    return '%02d_%02d_%s' % (int(main_num), int(sub_num), text)


def do_replace(root_path):
    file_list = os.listdir(root_path)
    for file_name in file_list:
        new_name = re.sub(r'\d{1,2}\s*-\s*\d{1,2}\s*-\s*(\d{1,2})\s*-\s*(\d{1,2})\s*(.+)', rename, file_name)
        cmd = 'mv \'%s\' \'%s\'' % (os.path.join(root_path, file_name), os.path.join(root_path, new_name))
        print(cmd)
        subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    folder = sys.argv[1]
    do_replace(folder)
