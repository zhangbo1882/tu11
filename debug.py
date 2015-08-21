#import os
from scrapy.cmdline import execute

#os.system("scrapy crawl dmoz -o item.csv")
argv=['scrapy','crawl', 'tu11']
execute(argv)