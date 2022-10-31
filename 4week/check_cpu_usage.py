'''
#!/usr/bin/env python3
'''
import psutil
import shutil
import emails
import os

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    #print(usage)
    if usage >= percent:

        message = 'Error - CPU usage is over 80%'
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
    percent = 80
    message = check_cpu_usage(percent)
    print(message)

'''
if not check_cpu_usage(80):
    print("Error - CPU usage is over 80%")
else:
    print("Everything ok")
'''