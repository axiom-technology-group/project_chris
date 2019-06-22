from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "51auto"])
# execute(["scrapy", "crawl", "ijiaotong"])
# execute(["scrapy", "crawl", "ksbbs"])
execute(["scrapy", "crawl", "chinadaily"])