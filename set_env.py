import subprocess
import re

"""
一键设置常用的环境变量
"""

envs = [
    ('JAVA_HOME', r'C:\Walter\development\jdk1.8.0_232'),
    ('MAVEN_HOME', r'C:\Walter\development\apache-maven-3.5.3'),
    ('ERLANG_HOME', r'C:\Walter\development\erl5.10.4'),
    ('ZOOKEEPER_HOME', r'C:\Walter\development\zookeeper-3.4.14')
]

GET_ENV = r'set {key}'
SET_ENV = r'setx {key} "{value}"'


def set_env(key, value):
    print('{} = {}'.format(key, value))
    set_cmd = SET_ENV.format(key=key, value=value)
    adb_proc = subprocess.Popen(set_cmd,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True)
    (output, err) = adb_proc.communicate()
    print(output.decode('gbk'))
    print(err.decode('gbk'))


path_env = ''
for item in envs:
    path_env = r'{}%{}%\bin;'.format(path_env, item[0])
    set_env(item[0], item[1])

old_path = r'C:\Users\ILove\anaconda3;' \
           r'C:\Users\ILove\anaconda3\Library\mingw-w64\bin;' \
           r'C:\Users\ILove\anaconda3\Library\usr\bin;' \
           r'C:\Users\ILove\anaconda3\Library\bin;' \
           r'C:\Users\ILove\anaconda3\Scripts;' \
           r'%USERPROFILE%\AppData\Local\Microsoft\WindowsApps;' \
           r'C:\Program Files\Bandizip\;' \
           r'C:\Users\ILove\AppData\Roaming\npm;' \
           r'C:\Users\ILove\AppData\Local\Programs\Microsoft VS Code\bin;'
set_env('Path', '{}{}'.format(old_path, path_env))
