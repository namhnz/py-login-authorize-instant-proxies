from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from random import randrange

s = Service(ChromeDriverManager().install())
op = webdriver.ChromeOptions()
op.add_argument(r"start-maximized")
op.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s, options=op)
driver.maximize_window()

# Dang nhap vao InstantProxies
driver.get(r"http://admin.instantproxies.com/login.php")
sleep(randrange(5))

userIdValue = ""
passwordValue = ""

with open("credential.txt", "r") as cre:
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

# Thuc hien chuc nang them ip vao danh sach cho phep
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
authedIpListString = driver.find_element(
    By.ID, r"authips-textarea").get_attribute("value")
print("Danh sach IP da duoc cho phep: " + authedIpListString)
authedIpList = str(authedIpListString).splitlines()
dupplicateAuthedIpList = set(
    [ip for ip in authedIpList if authedIpList.count(ip) > 1])
# Neu khong co dia chi ip trung thi ip do chua duoc them vao truoc day
if not len(dupplicateAuthedIpList):
    SubmitNewAuthedIpList()

# Dang xuat va thoat driver
signOutButton = driver.find_element(
    By.XPATH, r'//*[@id="top_container"]/div[3]/div/div/div/div[2]/input')
signOutButton.click()
print("Hoan thanh them dia chi ip hien tai vao danh sach cho phep")
sleep(1)
driver.close()
print("Da thoat trinh duyet")
