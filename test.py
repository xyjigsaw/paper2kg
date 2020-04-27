# Name: test
# Author: Reacubeth
# Time: 2020/4/26 22:18
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

import os

cmd = 'java -Xmx512m -jar toolkit/Ollie/ollie-app-latest.jar --malt-model toolkit/Ollie/engmalt.linear-1.7.mco -s -o work.txt 8.xml'
os.system(cmd)
