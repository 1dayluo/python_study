import os

path='F:/Geekhome/网络课程/麻瓜编程/day1/files/files'
myfiles = os.listdir(path)
print(path)
for f in myfiles:
    if not f.endswith('gif') and 'project30' in f or 'commercial' in f:
        print('Found : ' + f)