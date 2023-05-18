#!/usr/bin/env python


import os
import string


# 文件列表,包括子目录
def get_files_all(path, ext: []):
    dir_list = []
    doc_list = []
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                if os.path.isdir(file):
                    dir_list.append(file)
                else:
                    if len(ext) == 0:
                        doc_list.append(os.path.join(root, file))
                    elif get_file_ext(file) in ext:
                        doc_list.append(os.path.join(root, file))
    except Exception as e:
        print(e)
        return

    return doc_list, dir_list


# 获取当前文件夹文件，不搜索子目录
def get_files(path, ext: []):
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
            if len(ext) == 0:
                doc_list.append(os.path.join(path, file))
            elif get_file_ext(file) in ext:
                doc_list.append(os.path.join(path, file))
            else:
                pass
    return doc_list, dir_list


# 获取新文件的输出路径，与旧文件在同一目录
def get_output_path(source_file, ext, out_put_dir=""):
    file_real_path = os.path.split(os.path.realpath(source_file))
    file_shot_name = get_file_shot_name(source_file)
    out_file_name = os.path.join(os.path.join(file_real_path[0]), file_shot_name + ext)
    if out_put_dir != "":
        out_file_name = os.path.join(out_put_dir, file_shot_name + ext)
    return out_file_name


# 获取不带后缀的文件名
def get_file_shot_name(source_file):
    return os.path.splitext(os.path.basename(source_file))[0]


# 文件路径
def get_file_path(source_file):
    return os.path.split(os.path.realpath(source_file))[0]


# 文件扩展名
def get_file_ext(source_file):
    return os.path.splitext(source_file)[-1][1:]


def is_dir(path):
    return os.path.isdir(path)


def get_disklist():
    disk_list = []
    for c in string.ascii_uppercase:
        disk = c + ':/'
        if os.path.isdir(disk):
            disk_list.append(disk)
    return disk_list
