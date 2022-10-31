'''
#!/usr/bin/env python3
'''
import psutil
import shutil
import emails
import os

def check_free_space(percent):
    total, used, free = shutil.disk_usage(__file__)
    if free <= percent:
        message = "Error - Available disk space is less than 20%"
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = message
        #body: The same summary from the PDF, but using \n between the lines
        body = "Please check your system and resolve the issue as soon as possible"
    # emails: def generate(sender, recipient, subject, body, attachment_path):
        message = emails.generate_error(sender, receiver, subject, body)
        emails.send(message)
    else:
        message = "Everything is OK"
    
    return message

    #return free_space
    #return free_space < percent
if __name__ == "__main__":
    percent = 20
    message = check_free_space(percent)
    print(message)

#if not check_free_space(20):
    #print("Error - Available disk space is less than 20%")
#else:
    #print("Everything ok")