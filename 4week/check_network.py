'''
#!/usb/bin/env python3
'''

import os


def check_network(hostname):
    # On Windows ping once
    response = os.system("ping -n 1 " + hostname)
    # # On Linux ping once
    # # but on Windows ping four times
    # response = os.system("ping -c 1 " + hostname)
    #response = os.system("ping -c 1 " + hostname)
    if response != 0:
        message = 'Error - localhost cannot be resolved to 127.0.0.1'
    else:
        message = 'Everything is OK'

    return message



if __name__ == "__main__":
    hostname = "localhost"
    message = check_network(hostname)
    print(message)