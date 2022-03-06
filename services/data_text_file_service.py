from datetime import datetime
from typing import Optional, Union
from linqit import List;


# Doc ghi file chua thong tin dia chi IP da duoc cho phep

authedIpListDataTextFilePath = r"instant_proxies_data\authed_ip_list.txt";

def WriteAuthedIpListToDataTextFile(authedIpList: List) -> None:
    with open(authedIpListDataTextFilePath, "w") as authedIpListFile:
        for ip in authedIpList:
            authedIpListFile.write(ip + "\n");

    print("Da ghi xong danh sach ip duoc cho phep vao file");
    return None;

# Chon kieu return trong function: https://stackoverflow.com/a/52264392/7182661
def ReadAuthedIpListFromDataTextFile() -> Optional[List]:
    with open(authedIpListDataTextFilePath, "r") as authedIpListFile:
        authedIpList = List([line.rstrip() for line in authedIpListFile]);
        return authedIpList if len(authedIpList) > 0 else None;


# Doc ghi file chua thong tin proxy tu InstantProxies

providedProxyListDataTextFilePath = r"instant_proxies_data\provided_proxy_list.txt";
dateTimeFormatStyle = r"%b %d %Y %I:%M%p";

def WriteProvidedProxyListToDataTextFile(providedProxyList: List) -> None:
    now = datetime.now() # current date and time
    nowString = now.strftime(dateTimeFormatStyle);
    proxyListCount = len(providedProxyList);
    print("Tong so proxy duoc su dung: " + str(proxyListCount));

    with open(providedProxyListDataTextFilePath, "w") as providedProxyListFile:
        providedProxyListFile.write(nowString + "\n");
        providedProxyListFile.write(str(proxyListCount) + "\n");
        for proxy in providedProxyList:
            providedProxyListFile.write(proxy + "\n");

    print("Da ghi xong danh sach proxy vao file");
    return None;


# Chon kieu return trong function: https://stackoverflow.com/a/52264392/7182661
def ReadProvidedProxyListFromDataTextFile() -> Optional[Union[datetime, int, List]]:
    with open(providedProxyListDataTextFilePath, "r") as providedProxyListFile:
        writeTimeString = providedProxyListFile.readline().rstrip();
        # Neu chua co du lieu truoc do
        if writeTimeString == "":
            return None;
        else: 
            writeTime = datetime.strptime(writeTimeString, dateTimeFormatStyle);
            proxyListCount = int(providedProxyListFile.readline().rstrip());
            providedProxyList = List(range(proxyListCount)).select(lambda _: providedProxyListFile.readline().rstrip());

            return writeTime, proxyListCount, providedProxyList;