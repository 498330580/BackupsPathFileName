# -*- coding: UTF-8 -*-
import os
import datetime


# 获取当前时间
now_time = datetime.datetime.now()
# 格式化时间字符串
str_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
# 初始化存储
data = {"time": str_time, "data": []}


# 扫描指定目录，并返回目录下所有文件夹与文件结构字典
def scan_files(path: str, code: int):
    next_data = []
    files = []
    for item in os.scandir(path):
        if not item.is_dir():
            files.append(item.name)
        if item.is_dir():
            next_data.append(scan_files(str(item.path), code + 1))
    path_data = {"path": path, "next_data": next_data, "files": files}
    return path_data


# 读取data目录中的txt，返回分行列表
def read_txt(path):
    """
    path: path_list.txt文件路径
    """
    with open(path, "r") as f:
        print(f)


# 保存扫描后的数据为json
def save_json(path: str, data: dict):
    """
    path: 保存路径
    data：需要保存的数据
    """
    pass


# 主函数
def main():
    pass

if __name__ == '__main__':
    path = r'D:\Downloads\网易云音乐'
    data_files = scan_files(path, 0)
    data["data"] = data_files
    print(data)
