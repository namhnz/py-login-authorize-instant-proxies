from datetime import datetime
from typing import Optional, Union
from linqit import List
import os
from services.constants import data_file_constants


class InstantProxiesDataFileService:
    def __init__(self) -> None:
        self._authedIpsDataFilePath = data_file_constants.AUTHED_IPS_DATA_FOLDER_PATH + \
            r"/" + data_file_constants.AUTHED_IPS_DATA_FILE_NAME
        self._providedProxiesDataFilePath = data_file_constants.PROVIDED_PROXIES_DATA_FOLDER_PATH + \
            r"/" + data_file_constants.PROVIDED_PROXIES_DATA_FILE_NAME

    def _WriteAuthedIpsToDataFile(self, authedIps: List) -> None:
        if not os.path.exists(self._authedIpsDataFilePath):
            # Thu muc khong ton tai
            os.makedirs(data_file_constants.AUTHED_IPS_DATA_FOLDER_PATH)
            print("Da tao thu muc chua danh sach IP duoc cho phep")

        with open(self._authedIpsDataFilePath, "w+") as authedIpsDataFile:
            # Ghi dong tieu de cot
            for ip in authedIps:
                authedIpsDataFile.write(ip + "\n")

        print("Da ghi xong danh sach IP duoc cho phep vao file")

    # Chon kieu return trong function: https://stackoverflow.com/a/52264392/7182661
    def _ReadAuthedIpsFromDataFile(self) -> Optional[List]:
        if os.path.exists(self._authedIpsDataFilePath):
            with open(self._authedIpsDataFilePath, "r") as authedIpsDataFile:
                authedIpList = List([line.rstrip()
                                    for line in authedIpsDataFile])
                print("Da doc xong danh sach IP duoc cho phep da luu truoc do")
                return authedIpList if len(authedIpList) > 0 else None
        else:
            print("Khong co IP cho phep nao da duoc luu truoc do")
            return None

    def _WriteProvidedProxiesToDataFile(self, providedProxies: List) -> None:
        if not os.path.exists(self._providedProxiesDataFilePath):
            # Thu muc khong ton tai
            os.makedirs(data_file_constants.PROVIDED_PROXIES_DATA_FOLDER_PATH)
            print("Da tao thu muc chua danh sach proxy duoc cung cap")

        now = datetime.now()  # current date and time
        nowString = now.strftime(dateTimeFormatStyle)
        proxiesCount = len(providedProxies)
        print("Tong so proxy duoc cung cap: " + str(proxiesCount))

        with open(self._providedProxiesDataFilePath, "w+") as providedProxiesDataFile:
            providedProxiesDataFile.write(nowString + "\n")
            providedProxiesDataFile.write(str(proxiesCount) + "\n")
            for proxy in providedProxies:
                providedProxiesDataFile.write(proxy + "\n")

        print("Da ghi xong danh sach proxy duoc cung cap vao file")

    # Chon kieu return trong function: https://stackoverflow.com/a/52264392/7182661
    def _ReadProvidedProxiesFromDataFile(self) -> Optional[Union[datetime, int, List]]:
        if os.path.exists(self._providedProxiesDataFilePath):
            with open(self._providedProxiesDataFilePath, "r") as providedProxiesDataFile:
                wroteTimeString = providedProxiesDataFile.readline().rstrip()
                # Neu chua co du lieu truoc do
                if wroteTimeString == "":
                    print("Da doc xong danh sach proxy duoc cung cap vao file")
                    return None
                else:
                    writeTime = datetime.strptime(
                        wroteTimeString, data_file_constants.PROVIDED_PROXIES_DATA_FILE_DATE_TIME_FORMAT_STYLE)
                    proxyListCount = int(
                        providedProxiesDataFile.readline().rstrip())
                    providedProxyList = List(range(proxyListCount)).select(
                        lambda _: providedProxiesDataFile.readline().rstrip())

                    print("Da doc xong danh sach proxy duoc cung cap vao file")
                    return writeTime, proxyListCount, providedProxyList
        else:
            print("Khong co proxy duoc cung cap nao da duoc luu truoc do")
            return None
