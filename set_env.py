import subprocess
import re

"""
一键设置常用的环境变量
"""

envs = [
    ('JAVA_HOME', r'C:\Walter\development\jdk1.8.0_232'),
    ('MAVEN_HOME', r'C:\Walter\development\apache-maven-3.5.3'),
    ('ZOOKEEPER_HOME', r'C:\Walter\development\zookeeper-3.4.14')
]

GET_ENV = r'set {key}'
SET_ENV = r'setx {key} "{value}"'


def set_env(key, value):
    get_cmd = GET_ENV.format(key=key)
    adb_proc = subprocess.Popen(get_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                shell=True)
    (output, err) = adb_proc.communicate()
    env = output.decode('gbk')
    old_value = ''
    if env is not None and env != '':
        m = re.match(r'^\w+?=(.*)', env)
        if m:
            old_value = m.group(1)

    if old_value is not None and old_value != '':
        value = '{};{}'.format(value, old_value)
    set_cmd = SET_ENV.format(key=key, value=value)
    adb_proc = subprocess.Popen(set_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                shell=True)
    (output, err) = adb_proc.communicate()
    print(output.decode('gbk'))
    print(err.decode('gbk'))


for item in envs:
    set_env(item[0], item[1])
