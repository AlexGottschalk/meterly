import logging
import multiprocessing
import sys

import psutil
from joblib.parallel import Parallel, delayed

def get_logger():
    logger = logging.getLogger()
    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[%(process)d/%(processName)s] %(message)s")
        handler.setFormatter(formatter)
        handler.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger

def fn1(n):
    get_logger().debug("fn1(%d); cpu# %d", n, psutil.Process().cpu_num())

if __name__ == "__main__":
    get_logger().debug("main")
    Parallel(n_jobs=multiprocessing.cpu_count())(delayed(fn1)(n) for n in range(1, 101))