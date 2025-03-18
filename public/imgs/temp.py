import os 
import re
import json

# get all files from illustrations
files = os.listdir('public/imgs/illustrations')
# split the file name by - into 2 parts
# first part is the name of the illustration
# second part is the date
# sort the files by date
items=[]
# use regex to split the file name
# like 闪光菠萝皮_20240910.avif => ['闪光菠萝皮', '20240910']
pattern = re.compile(r'(.+?)_(\d+)\.avif')
pairs = [pattern.match(file).groups() for file in files if pattern.match(file)]


for pair in pairs:
    items.append({
        'illustrator': pair[0],
        "illustrator_contact": {},
        'date': pair[1],
        "description": "",
        "length": 0,
    })

# sort pair by date
items.sort(key=lambda x: x['date'], reverse=True)

print(items)
# write file with json format
with open('public/imgs/illustrations.json', 'w') as f:
    f.write(json.dumps(items, indent=4, ensure_ascii=False))