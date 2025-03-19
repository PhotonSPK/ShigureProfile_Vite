import os 
import re
import json

# get all files from illustrations
files = os.listdir('public/imgs/illustrations/绊理_20250210')
files.sort(key=lambda x: int(re.sub('\D', '', x)))
for i, file in enumerate(files):
    os.rename(f'public/imgs/illustrations/绊理_20250210/{file}', f'public/imgs/illustrations/绊理_20250210/{i:02d}.avif')
print(files)