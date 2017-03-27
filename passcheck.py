from itertools import product
from string import ascii_lowercase
from string import ascii_letters
from string import ascii_uppercase
import urllib2
import socket
from datetime import datetime

def CheckAxisURL(address,passwd):
    cameraurl = 'http://' + address + '/axis-cgi/param.cgi?action=list&group=root.Brand.ProdNbr'
    errorcode = ''
    try:
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, cameraurl, 'root', passwd)
        urllib2.install_opener(urllib2.build_opener(urllib2.HTTPDigestAuthHandler(passman)))
        f = urllib2.urlopen(cameraurl, timeout=3)
        cameramodel = f.read().split('=')
        f.close()
    except socket.timeout as e:
        errorcode = "Connection Timeout"
    except urllib2.HTTPError, e:
        if e.code == 404:
            errorcode = "Page not found"
        elif e.code == 403:
            errorcode = "Access denied"
        elif e.code == 401:
            errorcode = "Bad password"
        else:
            errorcode = "Something else happened"
    except urllib2.URLError:
        errorcode = "URL Error"
    if errorcode:
        return False
    else:
        return True


passbase = raw_input("Please enter the base password: ")
camaddr = raw_input("Please enter the camera IP address: ")

# print CheckAxisURL(camaddr,passbase)

keywords = [''.join(i) for i in product(ascii_uppercase, repeat = 3)]

# keywords = ['pass', 'root', 'admin']

# keywords.append(passbase)

for prefix in keywords:
    if CheckAxisURL(camaddr,prefix+passbase):
        print "Password found: " + prefix
        break

# for prefix in keywords:
#     print prefix + passbase
#
# print "Generated " + str(len(keywords)) + " passwords"
