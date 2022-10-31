'''
#!/usr/bin/env python3
'''

import os
import emails

def check_network(hostname):
    # On Windows ping once
    response = os.system("ping -n 1 " + hostname)
    # # On Linux ping once
    # # but on Windows ping four times
    # response = os.system("ping -c 1 " + hostname)
    #response = os.system("ping -c 1 " + hostname)
    if response != 0:
        message = 'Error - localhost cannot be resolved to 127.0.0.1'
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
    hostname = "localhost"
    message = check_network(hostname)
    print(message)