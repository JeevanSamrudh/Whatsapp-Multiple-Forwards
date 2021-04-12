from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options
import pyautogui as auto

auto.PAUSE=0.2
path = r"C:\Users\91807\Desktop\Project\DOTD\New\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
#Change chrome driver path accordingly
chrome_driver = path
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
#print (driver.current_url)
driver.minimize_window()
driver.maximize_window()

mouse_positions=[(129,282),(849,486),(585,229),(498,360),(835,588),(919,485)]

def first_photo_select():
    search_x_path='//*[@id="side"]/div[1]/div/label/div/div[2]'
    driver.find_element_by_xpath(search_x_path).send_keys('9901506070')
    auto.moveTo(mouse_positions[0],duration=0.6)
    auto.click()
    auto.moveTo(mouse_positions[1],duration=0.5)
    auto.click()
    

def send_to_all(num:list,last:int):
    if len(num) != 0:
        auto.moveTo(mouse_positions[2],duration=0.5)
        auto.click()
        auto.hotkey('ctrl','a')
        auto.write(str(num[0]))
        auto.moveTo(mouse_positions[3],duration=0.5)
        auto.click()
        return send_to_all(num[1:],last)
    else:
        auto.moveTo(mouse_positions[4],duration=0.5)
        auto.click()
        if last != 1:
            time.sleep(5)
            auto.moveTo(mouse_positions[5],duration=2.0)
            auto.click()
        else:
            auto.alert("Sent to all!")
        return

def num_alloc():
    file1 = open("numbers.txt","r")
    all_num = file1.readlines()
    all_num = [i[:10] for i in all_num ]
    while(len(all_num) != 0):
        num=all_num[:5]
        all_num=all_num[5:]
        if len(all_num) != 0:
            send_to_all(num,0)
        else:
            send_to_all(num,1)

def practice():
    l=[1,2,3]
    print(auto.position())
    return

first_photo_select()
#practice()
num_alloc()
#send_to_all(['8073960625','9901506070'],1)
