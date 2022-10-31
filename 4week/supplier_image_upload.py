'''
#!/usr/bin/env python3
'''

import os
#import requests

# This example shows how a file can be uploaded using
# The Python Requests module

# from example_upload.py
#url = "http://localhost/upload"
#with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#    r = requests.post(url, files={'file': opened})

# Check by visiting the URL [linux-instance-IP-Address]/media/images/
# Use the Python requests module to send the file contents
# to the [linux-instance-IP-Address]/upload URL.

#url = "http://34.27.49.107/upload/"

url = "[linux-instance-IP-Address]/upload"

# Generate a list of image files
path = "C:/a_Python/a_google_course/a_final_project/4week/newimages/"
images_list = os.listdir(path)
print(images_list)


for each in images_list:
    print(each)
    with open(each, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
