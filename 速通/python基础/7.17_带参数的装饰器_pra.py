import functools
import random
import time

#带参数的装饰器
def timer(max):
    def decorator(func):
        @functools.wraps(func)#这里相当于让新生成的wrapper完全继承了原来的func
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            time_cost = end - start
            if time_cost > max:
                print(f"{func.__name__}运行了超过阈值{time_cost}秒")
            return result
        return wrapper
    return decorator

@timer(3)
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

download("PDF")

