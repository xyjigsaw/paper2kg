# Name: readXML
# Author: Reacubeth
# Time: 2020/4/26 22:07
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*

from xml.dom.minidom import parse

# 读取文件
dom = parse('8.xml')
# 获取文档元素对象
data = dom.documentElement
# 获取 student
secs = data.getElementsByTagName('sec')
for item in secs:
    sec_title = item.getElementsByTagName('title')[0].childNodes[0].nodeValue
    print(sec_title)

#
ref_ls = data.getElementsByTagName('ref')
for item in ref_ls:
    article_title = item.getElementsByTagName('mixed-citation')[0].\
        getElementsByTagName('article-title')[0].childNodes[0].nodeValue
    print(article_title)

'''
# 获取标签属性值
    st_id = stu.getAttribute('id')
    st_name = stu.getAttribute('name')
    # 获取标签中内容
    id = stu.getElementsByTagName('id')[0].childNodes[0].nodeValue
    name = stu.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = stu.getElementsByTagName('age')[0].childNodes[0].nodeValue
    gender = stu.getElementsByTagName('gender')[0].childNodes[0].nodeValue
    print('st_id:', st_id, ', st_name:', st_name)
    print('id:', id, ', name:', name, ', age:', age, ', gender:', gender)
'''
