import os
import filecmp

path = 'F:/Geekhome/网络课程/麻瓜编程/day2/problem3_files/problem3_files'





dir2 = ['pic1', 'pic2']

def get_all_files(path,dirs):
    piclist = []
    for d in dirs:
        curpath = path + '/' + d
        files = os.listdir(curpath)
        for f in files:
            piclist.append(curpath + '/' + f)
    return piclist

def cmp_files(x,y):
         if filecmp.cmp(x, y):
            os.remove(y)
            print("路径\"" + y + "\"下的文件是重复文件，已经删除")


m = get_all_files(path, dir2)

for x in m:
    for y in m:
        if x!=y and os.path.exists(x) and os.path.exists(y):
            cmp_files(x,y)
