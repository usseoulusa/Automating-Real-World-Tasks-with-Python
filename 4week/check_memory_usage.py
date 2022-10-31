'''
#!/usr/bin/env python3
'''
import psutil
import shutil
import emails
import os

''' https://psutil.readthedocs.io/en/latest/#memory
>>> import psutil
>>> mem = psutil.virtual_memory()
>>> mem
svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712, active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304, slab=199348224)
>>>
>>> THRESHOLD = 100 * 1024 * 1024  # 100MB
>>> if mem.available <= THRESHOLD:
...     print("warning")
...
>>>
'''

def check_memory_usage(threshold):
    message = ''
    mem = psutil.virtual_memory()
    giga = threshold / (1024 * 1024 * 1024)
    if mem.available <= threshold:
        message = 'Error - Available memory is less than 500MB'
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = message
        #body: The same summary from the PDF, but using \n between the lines
        body = "Please check your system and resolve the issue as soon as possible"
    # emails: def generate(sender, recipient, subject, body, attachment_path):
        message = emails.generate_error(sender, receiver, subject, body)
        emails.send(message)
    else:
        message = 'Everything is OK'

    return message


if __name__ == "__main__":
    #threshold = 500 * 1024 * 1024  # 500MB
    #threshold = 1024 * 1024 * 1024 # 1,000MB = 1GB
    threshold = 7 * 1024 * 1024 * 1024 # 7GB
    message = check_memory_usage(threshold)
    print(message)