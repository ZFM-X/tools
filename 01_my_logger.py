import logging
import os


# 自定义过滤器
class myfileter(logging.Filter):
    def filter(self, record):
        return record.levelno >= logging.DEBUG


def mylogger(logger_name):
    '''
    定义日志处理器
    '''
    # 定义记录器
    logger = logging.getLogger(f"{logger_name}")
    logger.setLevel(logging.DEBUG)
    
    # 定义文件处理器
    file_hanlder = logging.FileHandler(os.path.join(os.path.split(os.path.realpath(__file__))[0], f'{logger_name}.log'), mode='w', encoding='utf-8')
    file_hanlder.setLevel(logging.DEBUG)
    
    # 定义控制台处理器
    stream_hanlder = logging.StreamHandler()
    stream_hanlder.setLevel(logging.DEBUG)
    
    # 定义格式器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(pathname)s - %(message)s')
    file_hanlder.setFormatter(formatter)
    stream_hanlder.setFormatter(formatter)
    
    # 处理器加入记录器和过滤器
    logger.addHandler(file_hanlder)
    logger.addHandler(stream_hanlder)
    logger.addFilter(myfileter())
    logger.info('日志采集开始')
    
    return logger

if __name__ == '__main__':
    mylogger('日志测试')