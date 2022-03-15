from ntpath import join
from services.current_machine_ip import getIp;
from linqit import List;
from services.instant_proxies_service import *;
from services.data_text_file_service import *;
from datetime import datetime, timedelta;
from services.data_file_service import InstantProxiesDataFileService;

# Lay dia chi IP cua may tinh hien tai
currentMachineIp = getIp();

# Khoi tao chuc nang ghi danh sach IP cho phep va proxy duoc cung cap
dataFileService = InstantProxiesDataFileService();

# Kiem tra xem dia chi IP dang su dung co nam trong danh sach ip duoc cho phep da luu truoc do khong
authedIpList = dataFileService._ReadAuthedIpsFromDataFile();
if authedIpList != None and authedIpList.contains(currentMachineIp):
    # Neu dia chi IP hien tai cua may da co trong danh sach duoc cho phep
    pass;
else:
    # Neu dia chi IP chua them vao danh sach cho phep thi tien hanh vao trang InstantProxies de them
    SignInInstantProxies();
    # Trang InstantProxies tu dong phat hien dia chi IP dang su dung nen khong can truyen vao dia chi IP cua may hien tai
    newAuthedIpList = AddMachineIpToWebAuthedIpList();
    dataFileService._WriteAuthedIpsToDataFile(newAuthedIpList);
    SignOutInstantProxies();
    

# Kiem tra danh sach proxy da luu proxy nao hay chua
forCrawlDataProxyList = List();
proxyListData = dataFileService._ReadProvidedProxiesFromDataFile();
if proxyListData != None:
    writeTime, proxyListCount, providedProxyList = proxyListData;
    # Neu thoi gian luu file proxy den hien tai qua 24 gio thi vao web InstantProxies de lay danh sach proxy moi: https://stackoverflow.com/a/26313848/7182661
    if (datetime.now() - writeTime) < timedelta(hours=24): 
        # less than 24 hours passed
        forCrawlDataProxyList = providedProxyList;
    else:
        # Lam moi danh sach proxy tu web InstantProxies
        SignInInstantProxies();
        newProvidedProxyList = GetProxyListOnWeb();
        dataFileService._WriteProvidedProxiesToDataFile(newProvidedProxyList);
        SignOutInstantProxies();
        forCrawlDataProxyList = newProvidedProxyList;
else:
    # Lam moi danh sach proxy tu web InstantProxies
    SignInInstantProxies();
    newProvidedProxyList = GetProxyListOnWeb();
    dataFileService._WriteProvidedProxiesToDataFile(newProvidedProxyList);
    SignOutInstantProxies();
    forCrawlDataProxyList = newProvidedProxyList;

print("Danh sach proxy duoc su dung de crawl du lieu: " + " ".join(forCrawlDataProxyList));
