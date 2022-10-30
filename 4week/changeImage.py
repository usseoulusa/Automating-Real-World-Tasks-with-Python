
'''
#!/usr/bin/env python3
'''


''' Requirement
1. Size: Change image resolution from 3000x2000 to 600x400 pixel
2. Format: Change image format from .TIFF to .JPEG
3. After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.
'''


import os
#import shutil
from PIL import Image


#path = "/home/student-00-cc3d6b059d40/images/"
path = "C:/a_Python/a_google_course/a_final_project/4week/images/"

# This must be ~/supplier-data/images
#save_path = "/opt/icons/"
save_path = "C:/a_Python/a_google_course/a_final_project/4week/newimages/"

#dir_list = os.listdir(path)
#print(dir_list)

# to store files in a list
#list = []


for (root, dirs, file) in os.walk(path):
    for f in file:
        print(f)
        im = Image.open(root+f)
        # Size: Change image resolution from 3000x2000 to 600x400 pixel
        # Format: Change image format from .TIFF to .JPEG
        cov_im = im.convert("RGB")
        im.resize((600, 480)).convert('RGB').save(save_path+f+".jpeg")
        #im.rotate(270).resize((128, 128)).convert('RGB').save(save_path+f+".jpeg")
        #rgb_im = im.convert("RGB")
        #im.save(path+f)
        #print(new_root+f)
        #print(root+f)
        #print(save_path)
        #if '.tiff' in f:
        #print(f)
# file output
#run:
#file ic_near_me_black_48dp.jpeg
#:run

#output:
#ic_near_me_black_48dp.jpeg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 600x480, components 3
#:output
