from requests import get

# Lay dia chi IP cua may dang su dung: https://stackoverflow.com/a/36205547/7182661
def getIp():
    currentMachineIp = get('http://ipify.org/').content.decode('utf8');
    print('My public IP address is: {}'.format(currentMachineIp));
    return currentMachineIp;