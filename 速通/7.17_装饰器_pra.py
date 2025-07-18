import random
import sys
import time


def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}运行了{end-start}秒")
        return result
    return wrapper

download = decorator(download)
upload = decorator(upload)

download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')

#带参数的装饰器
def timer(max):
    def decorator(func):