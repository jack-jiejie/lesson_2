__author__ = "yin"
__data__ = "2020/4/5 20:46"

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname((os.path.abspath(__file__))))
execute(["scrapy", "crawl", "tieba"])



