import os
import sys
import time
# from appium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PIL import Image


def Get_Snap(driver, FileName):
    driver.save_screenshot(FileName)
    page_snap_obj = Image.open(FileName)
    return page_snap_obj


def Get_Image(driver, xPath, ImageName):
    img = driver.find_element(By.XPATH, xPath)
    # driver.implicitly_wait(20)
    element = WebDriverWait(driver, 15, 1).until(
        EC.presence_of_element_located((By.XPATH, xPath)))
    location = img.location
    size = img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    # print(left, top, right, bottom)
    page_snap_obj = Get_Snap(driver, ImageName)
    image_obj = page_snap_obj.crop((left, top, right, bottom))
    return image_obj


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
# 1. 使用Chrome App到國泰世華銀行官網(https://www.cathaybk.com.tw/cathaybk/)並將畫面截圖。
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.cathaybk.com.tw/cathaybk/")

try:
    charts = driver.find_element(By.CLASS_NAME, 'cubre-o-indexKv__pic')
    action = ActionChains(driver)
    action.move_to_element(charts).perform()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cubre-o-indexKv__pic')))
finally:
    driver.get_screenshot_as_file("CUBHome.png")


# 2. 點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。
button = driver.find_element(
    By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[1]")
button.click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@style='display: block;']")))
count = 0
if (driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]")):
    Get_Image(
        driver, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]", "CUBCardItem.png")
    CardName = driver.find_element(
        By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[1]")
    CardItemList = CardName.find_element(
        By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]")
    print("==========")
    print(CardItemList.text.split("\n"))
    print("項目:", len(CardItemList.text.split("\n")))
    print("==========")
    # driver.get_screenshot_as_file("CUBCardItem.png")

time.sleep(2)
# driver.close()

# 3. 個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖
CardInfobutton = driver.find_element(
    By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/a[1]")
CardInfobutton.click()

# 捜尋並點選"停發卡"選項
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/main/article/div/div/div/div[1]/div/div/a[6]/p")))
CardInfobutton = driver.find_element(
    By.XPATH, "/html/body/div/main/article/div/div/div/div[1]/div/div/a[6]/p")
CardInfobutton.click()
# 捜尋"停發卡"component
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/main/article/section[6]/div")))
StopCardList = []
if (driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]")):
    Get_Image(
        driver, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[1]", "CUBStopCard1.png")
    StopCard = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[1]")
    StopList = StopCard.text.split("\n")
    for CardList in StopList:
        if "停發" in CardList:
            StopCardList.append(CardList)

    Get_Image(
        driver, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[2]", "CUBStopCard2.png")
    StopCard = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[2]")
    StopList = StopCard.text.split("\n")
    for CardList in StopList:
        if "停發" in CardList:
            StopCardList.append(CardList)

    Get_Image(
        driver, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[3]", "CUBStopCard3.png")
    StopCard = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[3]")
    StopList = StopCard.text.split("\n")
    for CardList in StopList:
        if "停發" in CardList:
            StopCardList.append(CardList)

    StopCardbutton = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[4]")
    # Go to slide 2
    StopCardbutton.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']")))
    # Go to slide 3
    StopCardbutton.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']")))
    # Go to slide 4
    StopCardbutton.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']")))

    Get_Image(
        driver, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[4]", "CUBStopCard4.png")
    StopCard = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[4]")
    StopList = StopCard.text.split("\n")
    for CardList in StopList:
        if "停發" in CardList:
            StopCardList.append(CardList)

    Get_Image(
        driver, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[5]", "CUBStopCard5.png")
    StopCard = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[5]")
    StopList = StopCard.text.split("\n")
    for CardList in StopList:
        if "停發" in CardList:
            StopCardList.append(CardList)

    Get_Image(
        driver, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[6]", "CUBStopCard6.png")
    StopCard = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[6]")
    StopList = StopCard.text.split("\n")
    for CardList in StopList:
        if "停發" in CardList:
            StopCardList.append(CardList)

    # Go to slide 5
    StopCardbutton.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']")))
    Get_Image(
        driver, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[7]", "CUBStopCard7.png")
    StopCard = driver.find_element(
        By.XPATH, "/html/body/div/main/article/section[6]/div/div[2]/div/div[1]/div[7]")
    StopList = StopCard.text.split("\n")
    for CardList in StopList:
        if "停發" in CardList:
            StopCardList.append(CardList)

    StopCardList = list(dict.fromkeys(StopCardList))
    print("==========")
    print(StopCardList)
    print("停發卡:", len(StopCardList))
    print("==========")

time.sleep(2)
driver.close()

"""
/html/body/div/main/article/section[6]/div/div[2]/div/div[2]/span[1]

"""
