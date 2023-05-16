#!/usr/bin/env python


import os


# 文件列表
def file_list(path, ext=""):
    dir_list = []
    doc_list = []
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            if file[0] == ".":
                pass
            else:
                dir_list.append(file)
        else:
            if ext == "":
                doc_list.append(os.path.join(path, file))
            elif os.path.splitext(file)[1] == ext:
                doc_list.append(os.path.join(path, file))
            else:
                pass
    return doc_list


# 获取新文件的输出路径，与旧文件在同一目录
def get_output_path(source_file, ext):
    file_real_path = os.path.split(os.path.realpath(source_file))
    file_shot_name = get_file_shot_name(source_file)
    out_file_name = os.path.join(os.path.join(file_real_path[0]), file_shot_name + ext)
    return out_file_name


# 获取不带后缀的文件名
def get_file_shot_name(source_file):
    return os.path.splitext(os.path.basename(source_file))[0]


# 文件路径
def get_file_path(source_file):
    return os.path.split(os.path.realpath(source_file))[0]
