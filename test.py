# Name: test
# Author: Reacubeth
# Time: 2020/4/26 22:18
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from jpype import *
jvm_path = get_default_jvm_path()
startJVM(jvm_path, 'ea')
java.lang.System.out.println('Success')
shutdownJVM()
