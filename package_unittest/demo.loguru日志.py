# 1.下载 ：pip install loguru

# 2.导包 :
from loguru import logger

# 3.打印一条日志
logger.info('这是一条info日志') # info代表级别的意思

# 4.输出不同的日志，分别是debug, info ,warning, sunccess, error
logger.debug('这是一条debug日志')
logger.info('这是一条info日志')
logger.warning('这是一条warning日志')
logger.success('这是一条success日志')
logger.error('这是一条error日志')

# 5.输出到文件 ：add()
logger.add('a.log', format='{time:YYYY-MM-DD at HH:mm:ss} {level} {module} {line} {message}') # 添加到下面的日志才会输出
logger.debug('这是一条debug日志')
logger.info('这是一条info日志')
logger.warning('这是一条warning日志')
logger.success('这是一条success日志')
logger.error('这是一条error日志')

# 进行传入参数的格式化 ：
logger.info('我的名字叫{}','今天星期{}',张三,一)