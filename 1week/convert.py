
#!/usr/bin/env python3


import os
#import shutil
from PIL import Image


path = "/home/student-00-cc3d6b059d40/images/"
# This must be /opt/icons/
save_path = "/opt/icons/"

#dir_list = os.listdir(path)

#print(dir_list)

# to store files in a list
list = []


''' Requirement
1. Iterate through each file in the folder

2. For each file:
    a. Rotate the image 90° clockwise
    b. Resize the image from 192x192 to 128x128
    c. Save the image to a new folder in .jpeg format
'''
'''
for (root, dirs, file) in os.walk(path):
    for f in file:
        new_file = "{}.jpeg".format(f)
        shutil.copy(root+f, save_path+new_file)
'''

for (root, dirs, file) in os.walk(path):
    for f in file:
        #print(f)
        im = Image.open(root+f)
        #print(f'{f}.jpeg is image')
        #cov_im = im.convert("RGB")
        im.rotate(270).resize((128, 128)).convert('RGB').save(save_path+f+".jpeg")
        #rgb_im = im.convert("RGB")
        #im.save(path+f)
        #print(new_root+f)
        #print(root+f)
        #print(save_path)
        #if '.tiff' in f:
        #print(f)
