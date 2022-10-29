'''
#!/usr/bin/env python
'''

import os
import shutil
from PIL import Image


path = "c://a_Python//a_google_course//a_final_project//1week//images//"
save_path = "c://a_Python//a_google_course//a_final_project//1week//new_images//"
dir_list = os.listdir(path)

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

for (root, dirs, file) in os.walk(path):
    for f in file:
        new_file = "{}.jpeg".format(f)
        shutil.copy(root+f, save_path+new_file)

for (new_root, dirs, file) in os.walk(save_path):
    for f in file:
        #im = Image.open(new_root+f)
        #print(f'{f}.jpeg is image')
        #cov_im = im.convert("RGB")
        #im.rotate(270).resize((128, 128))
        #rgb_im = new_im.convert("RGB")
        #im.save(new_root+f)
        print(new_root+f)
        #print(save_path)
        #if '.tiff' in f:
            #print(f)
