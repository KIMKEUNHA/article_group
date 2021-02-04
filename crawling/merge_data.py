import json
import os
import time

path = '/home/seungho/woongjin/kim/article_group/crawling/data_news'
out_path = time.strftime('/home/seungho/woongjin/kim/article_group/crawling/%y_%m_%d_%H:%M_merge.json')
file_li = os.listdir(path)
idx = 0

opfile = {}
opfile['merge_fnames'] = []
opfile["time"] = time.strftime('%y-%m-%d %H:%M:%S')
opfile["document"] = []
for f_name in file_li:
    with open(path+"/"+f_name) as file:
        data = json.load(file)
        opfile['merge_fnames'].append(f_name)
        opfile["document"]+=data['document']
with open(out_path,"w") as output:
    json.dump(opfile,output,ensure_ascii=False,indent=4)