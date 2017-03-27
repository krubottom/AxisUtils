import urllib2
import socket

def GetAxisFirmwareVersion(address,passwd):
    cameraurl = 'http://' + address + '/axis-cgi/param.cgi?action=list&group=root.Properties.Firmware.Version'
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, cameraurl, 'root', passwd)
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPDigestAuthHandler(passman)))
    f = urllib2.urlopen(cameraurl)
    camerafw = f.read().split('=')
    f.close()
    return camerafw[1].rstrip()

def GetAxisCameraModel(address,passwd):
    cameraurl = 'http://' + address + '/axis-cgi/param.cgi?action=list&group=root.Brand.ProdNbr'
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, cameraurl, 'root', passwd)
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPDigestAuthHandler(passman)))
    f = urllib2.urlopen(cameraurl, timeout=3)
    cameramodel = f.read().split('=')
    f.close()
    return cameramodel[1].rstrip()


def GetAxisServerReport(address,passwd):
    cameraurl = 'http://' + address + '/axis-cgi/admin/systemlog.cgi'
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, cameraurl, 'root', passwd)
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPDigestAuthHandler(passman)))
    f = urllib2.urlopen(cameraurl)
    cameraserverreport = f.read().split('=')
    f.close()
    return cameraserverreport[1].rstrip()

def GetAxisTemp(address,passwd):
    cameraurl = 'http://' + address + '/axis-cgi/temperaturecontrol.cgi?device=sensor&id=0&action=query&temperatureunit=fahrenheit'
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, address, 'root', passwd)
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPDigestAuthHandler(passman)))
    f = urllib2.urlopen(cameraurl)
    cameratemp = f.read().rstrip()
    f.close()
    return cameratemp + 'F'

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
        return errorcode
    else:
        return 'Good URL'
