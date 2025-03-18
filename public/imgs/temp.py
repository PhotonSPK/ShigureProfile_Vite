import os 

# get all files from illustrations
files = os.listdir('public/imgs/illustrations')
# split the file name by - into 2 parts
# first part is the name of the illustration
# second part is the date
# sort the files by date
files = sorted(files, key=lambda x: x.split('-')[1])
print(files)
print(len(files))