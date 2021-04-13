import multiprocessing

bind = "127.0.0.1:8000"  # 绑定的ip与端口
workers = 2  # 核心数
errorlog = '/home/webserver/web/gunicorn.error.log'  # 发生错误时log的路径
accesslog = '/home/webserver/web/gunicorn.access.log'  # 正常时的log路径
# loglevel = 'debug'   #日志等级
proc_name = 'gunicorn_project'  # 进程名
