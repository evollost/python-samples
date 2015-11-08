# -*- coding: utf-8 -*-
#
# Copyright 2015-2016 ev0l

import json
import re

with open('../test.json') as f:
    #line = json.loads(f)
# print (line.decode('unicode_escape'))
    str = f.read()[1:-1]
    dict = json.loads(str)
    data = ''.join([i.encode('unicode_escape') for i in dict['desc']])
    #pattern = re.compile("\<a href=.*?\>|\<\/[abp]\>|\<[bp]\>|\<sup id=.*?\/sup\>")
    pattern = re.compile("\<p\>\<\/p\>.*|\<.*?\>|\[.*?\]")
    dict['desc'] = re.sub(pattern, '', data)
    print dict['desc'].decode('unicode_escape')