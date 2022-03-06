from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randrange
from linqit import List;

s = Service(ChromeDriverManager().install())
op = webdriver.ChromeOptions()
op.add_argument(r"start-maximized")
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=op)
driver.maximize_window()

def SignInInstantProxies():
    # Dang nhap vao InstantProxies
    driver.get(r"http://admin.instantproxies.com/login.php")
    sleep(randrange(5))

    userIdValue = ""
    passwordValue = ""

    with open(r"instant_proxies_data\credential.txt", "r") as cre:
        userIdValue = cre.readline().strip()
        passwordValue = cre.readline().strip()

    userIdInput = driver.find_element(By.ID, "user")
    userIdInput.send_keys(userIdValue)
    print("Da nhap xong user id")
    sleep(1)

    passwordInput = driver.find_element(By.ID, "password")
    passwordInput.send_keys(passwordValue)
    print("Da nhap xong password")
    sleep(1)

    signInButton = driver.find_element(By.ID, r'x')
    signInButton.click()
    print("Da nhan nut sign in")
    sleep(randrange(5))

def GetAuthedIpListOnWeb() -> List:
    authedIpListString = driver.find_element(
        By.ID, r"authips-textarea").get_attribute("value")
    print("Danh sach IP da duoc cho phep: " + authedIpListString)
    authedIpList = List(str(authedIpListString).splitlines());
    return authedIpList;

def AddMachineIpToWebAuthedIpList() -> List:
    # Thuc hien chuc nang them IP vao danh sach cho phep
    addAuthIpA = driver.find_element(By.ID, r"addauthip-link")
    addAuthIpA.click()
    print("Da them IP hien tai vao danh sach cho phep")
    sleep(randrange(2, 5))

    # Thuc hien chuc nang cap nhanh danh sach ip cho phep moi
    def SubmitNewAuthedIpList():
        submitNewIpListButton = driver.find_element(
            By.XPATH, r'//*[@id="top_container"]/div[3]/div/div/table/tbody/tr/td[3]/form/div/input')
        submitNewIpListButton.click()
        print("Da cap nhat danh sach IP cho phep moi")
        sleep(randrange(5))


    # Kiem tra ip hien tai da co trong danh sach cho phep chua
    authedIpList = GetAuthedIpListOnWeb();
    dupplicateAuthedIpList = set(
        [ip for ip in authedIpList if authedIpList.count(ip) > 1])
    # Neu khong co dia chi IP trung thi IP do chua duoc them vao truoc day
    if not len(dupplicateAuthedIpList):
        SubmitNewAuthedIpList()
        sleep(randrange(5));
    
    # Do sau khi nhan Submit va tai lai trang, dia chi IP moi mat tu 1-2 phut de them vao danh sach
    return List(set(authedIpList));
    
def GetProxyListOnWeb() -> List:
    # Vao trang chu co danh sach proxy
    driver.get(r"http://admin.instantproxies.com/main.php");
    sleep(randrange(5));

    # Lay danh sach proxy
    providedProxyListString = driver.find_element(By.ID, r"proxies-textarea").get_attribute("value");
    providedProxyList = List(providedProxyListString.split("\n"));
    return providedProxyList;


def SignOutInstantProxies():
    # Dang xuat va thoat driver
    signOutButton = driver.find_element(
        By.XPATH, r'//*[@id="top_container"]/div[3]/div/div/div/div[2]/input')
    signOutButton.click()
    print("Dang dang xuat khoi InstantProxies")
    sleep(1)
    # driver.close()
    # print("Da thoat trinh duyet")