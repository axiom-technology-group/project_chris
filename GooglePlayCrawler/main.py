from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# cmdline.execute("scrapy crawl gp -a urls='https://play.google.com/store/apps/details?id="
#                 # "id.danarupiah.weshare.jiekuan&hl=id'".split())

execute(["scrapy","crawl","gp_crawl","-o","data_end.csv"])