import multiprocessing


bind = "127.0.0.1:9900"
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2 + 1
