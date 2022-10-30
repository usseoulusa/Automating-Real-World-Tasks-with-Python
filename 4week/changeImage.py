
'''
#!/usr/bin/env python3
'''


''' Requirement
1. Size: Change image resolution from 3000x2000 to 600x400 pixel
2. Format: Change image format from .TIFF to .JPEG
'''


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
