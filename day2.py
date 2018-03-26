import os
import shutil

path = 'F:\Geekhome\网络课程\麻瓜编程\day1\problem2_files\problem2_files'
files = os.listdir(path)
folder_name_1 = path + '/image'
folder_name_2 = path + '/document'
os.makedirs(folder_name_1)
os.makedirs(folder_name_2)
for folder in files:
    cur_path_one = path + '/' + folder
    now_files = os.listdir(cur_path_one)
    if 'jpg' in folder or 'png' in folder or 'gif' in folder:
        for f in now_files:
            shutil.move(cur_path_one + '/' + f, folder_name_1)
    if 'doc' in folder or 'docx' in folder or 'md' in folder or 'ppt' in folder:
        for f in now_files:
            shutil.move(cur_path_one + '/' + f, folder_name_2)
    os.removedirs(cur_path_one)



