import multiprocessing

bind = "0.0.0.0:12000"
daemon = True
workers = multiprocessing.cpu_count() * 2 + 1