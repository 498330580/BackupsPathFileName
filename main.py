# -*- coding: UTF-8 -*-
import os
import sys
import datetime
import json


# 设定工作目录为当前脚本目录
jaoben_path = os.path.abspath(os.path.dirname(sys.argv[0])) # 当前脚本目录
os.chdir(jaoben_path)   # 设定工作目录为脚本目录


# 获取当前时间
now_time = datetime.datetime.now()
# 格式化时间字符串
str_time = now_time.strftime("%Y-%m-%d %H:%M:%S")
# 初始化存储
data = {"time": str_time, "data": []}


# 扫描指定目录，并返回目录下所有文件夹与文件结构字典
def scan_files(path: str, code: int = 0) -> dict:
    """
    path: 需要扫描的路径
    code: 路径层级(顶级为0)
    """
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
def read_txt(path: str) -> list:
    """
    path: path_list.txt文件路径
    """
    with open(path, "r", encoding='utf-8') as f:
        data = f.readlines()
    return data


# 保存扫描后的数据为json
def save_json(path: str, data: dict):
    """
    path: 保存路径
    data：需要保存的数据
    """
    with open(path, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# 运行判断
def run_one():
    # 判断path_list.txt文件是否存在，如果不存在则创建
    if not os.path.exists("./data/path_list.txt"):
        with open("./data/path_list.txt", "w", encoding="utf-8") as f:
            f.write("/video")


# 主函数
def main():
    print("开始运行")
    run_one()
    path_list = read_txt('./data/path_list.txt')
    path_data = []
    for path in path_list:
        path = path.strip()
        print(f"正在扫描：{path}")
        if os.path.exists(path):
            data_files = scan_files(path)
            path_data.append(data_files)
    data["data"] = path_data
    save_json("./data/data.json", data)
    print("扫描完毕")

if __name__ == '__main__':
    main()