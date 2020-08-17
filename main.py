from FaceBook_Reg import Facebook_bot
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json
import random
from random import sample
import threading
import time
import sys
import threading

user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0',  'Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                   'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'

                   ]

First_name = ["Nguyễn", "Võ", "Vũ", "Trần", "Lê", " Mạc", "Mai",
              " lý", "Đào", "Phạm", "Phan", "Đặng", "Ngô", "Hồ", "Dương", "Lâm", "Phi"]
last_name = ["Bảo Long", "Nghiêm", "Khả Như", "Bảo Anh", "Trâm Anh", "Ánh Tuyêt", "Bảo Lâm", "Mạnh Đức", "Phương", "Mai Phương", "Ly", "Thươn", "Nga", "Nhân", "Thảo", "Vinh", "Tùng", "Nghĩa", "Cương", "Đạt", "Duy", "Bảo Minh", "Duy Bảo", "Quốc Bảo", "Ðức Toàn", "Ðức Bình", "Đức Duy", "Tài Đức", "Phúc Lâm",  "Phúc Hưng",
             "Phúc Điền", "Giang", "Hà Anh", "Ngoc", "Tuyến", "Trung Hiếu", "Trọng Hiếu", "Thanh Hà", "Ngọc Hà ", "Lâm Hà", "Dung Hà", "Ánh", "Ngọc Ánh", "Thiên Ánh", "Anh", "Tuấn Anh", "Ngọc Anh", "Minh", "ngọc Minh", "Dung", "Hoang", "Nam", "Thang", "Cong", "Bảo Lâm", "Thiện", "Trung", "Ngọc Anh", "Hồng Vũ", "Diễm Phương", " Bích Phuong", "Thành", "Phúc",  "Hoàng Nam", "Hoàng Phong", "Hoàng Hải", "Hoàng Đăng", "Tùng Quân", "Hạo Nhiên",  "Hữu Phước", "Toàn Thắng", "Tuấn Kiệt", "Đăng Khoa", "Minh Quân", "Gia Hưng", "Dương Minh"]
First_number = ["086", "096", "097", "098", "032", "033", "034", "035", "036", "037", "038", "039", "089",
                "090", "093", "070", "079", "077", "076", "078", "088", "091", "094", "083", "084", "085", "081", "082", "092", "056", "058", "099", "059"]

phone_number_extension = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

locales = ["en", "es", "uk", "fr"]

Phone = []
frames = []
t_connectings = []
Join = []


class myThread1(threading.Thread):
    def __init__(self, url, telephones, passwords, first_names, last_names, user_agent, locale):
        threading.Thread.__init__(self)
        self.url = url
        self.telephones = telephones
        self.passwords = passwords
        self.first_names = first_names
        self.last_names = last_names
        self.user_agent = user_agent
        self.locale = locale

    def run(self):

        Facebook_bot.Sign_up(self.url, self.telephones, self.passwords,
                             self.first_names, self.last_names,  self.user_agent, self.locale)


class myThread2(threading.Thread):
    def __init__(self, url, telephones, passwords, first_names, last_names, user_agent, locale):
        threading.Thread.__init__(self)
        self.url = url
        self.telephones = telephones
        self.passwords = passwords
        self.first_names = first_names
        self.last_names = last_names
        self.user_agent = user_agent
        self.locale = locale

    def run(self):

        Facebook_bot.Sign_up(self.url, self.telephones, self.passwords,
                             self.first_names, self.last_names,  self.user_agent, self.locale)


class myThread3(threading.Thread):
    def __init__(self, url, telephones, passwords, first_names, last_names, user_agent, locale):
        threading.Thread.__init__(self)
        self.url = url
        self.telephones = telephones
        self.passwords = passwords
        self.first_names = first_names
        self.last_names = last_names
        self.user_agent = user_agent
        self.locale = locale

    def run(self):

        Facebook_bot.Sign_up(self.url, self.telephones, self.passwords,
                             self.first_names, self.last_names,  self.user_agent, self.locale)


class myThread4(threading.Thread):
    def __init__(self, url, telephones, passwords, first_names, last_names, user_agent, locale):
        threading.Thread.__init__(self)
        self.url = url
        self.telephones = telephones
        self.passwords = passwords
        self.first_names = first_names
        self.last_names = last_names
        self.user_agent = user_agent
        self.locale = locale

    def run(self):

        Facebook_bot.Sign_up(self.url, self.telephones, self.passwords,
                             self.first_names, self.last_names,  self.user_agent, self.locale)


class myThread5(threading.Thread):
    def __init__(self, url, telephones, passwords, first_names, last_names, user_agent, locale):
        threading.Thread.__init__(self)
        self.url = url
        self.telephones = telephones
        self.passwords = passwords
        self.first_names = first_names
        self.last_names = last_names
        self.user_agent = user_agent
        self.locale = locale

    def run(self):
        
        Facebook_bot.Sign_up(self.url, self.telephones, self.passwords,
                             self.first_names, self.last_names,  self.user_agent, self.locale)


lock = threading.Lock()

if __name__ == "__main__":
    localtime = time.localtime(time.time())
    user_agent = random.choice(user_agent_list)
    Ho = random.choice(First_name)
    Ten = random.choice(last_name)

    for i in range(1, 6, 1):
        phone_number_firt = random.choice(First_number)
        list_int = sample(phone_number_extension, 7)
        list_int_new = "".join(list_int)
        phone = phone_number_firt + list_int_new
        print(phone)
        Phone.append(phone)
    password = str(localtime[2])+str(phone)
    localess = random.choice(locales)
    print(password)
    print(phone)
    print(user_agent)
    thread1 = threading.Thread(target=Facebook_bot.Sign_up, args=("https://www.facebook.com/", Phone[0],
                                                                  password, random.choice(First_name), random.choice(last_name), random.choice(user_agent_list), random.choice(locales)), daemon=True)
    # myThread1("https://www.facebook.com/", Phone[0],
    #                 password, random.choice(First_name), random.choice(last_name), random.choice(user_agent_list), random.choice(locales))
    thread2 = threading.Thread(target=Facebook_bot.Sign_up, args=("https://www.facebook.com/", Phone[0],
                                                                  password, random.choice(First_name), random.choice(last_name), random.choice(user_agent_list), random.choice(locales)), daemon=True)

    while True:

        print("in")
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.privatebrowsing.autostart', True)
        driver = webdriver.Firefox(firefox_profile=profile)
        driver.get("http://192.168.0.86/")
        username = driver.find_elements_by_id("userName")
        password = driver.find_element_by_id("pcPassword")
        btn = driver.find_element_by_id("loginBtn")
        username[0].send_keys("admin")
        password.send_keys("admin")
        btn.click()
        time.sleep(3)
        for frame in driver.find_elements_by_xpath('.//frame'):
            frames.append(frame)
        print("Frame", frames[2])
        time.sleep(4)
        driver.switch_to.frame(frames[2])

        ids = driver.find_elements_by_id("Disconnect")
        ids[0].click()

        time.sleep(3)
        ids_connect = driver.find_elements_by_id("Connect")
        ids_connect[0].click()
        t_connecting = driver.find_elements_by_id("t_connecting")
        t_connectings.append(t_connecting)
        element = WebDriverWait(driver, 3000).until(
            EC.presence_of_element_located((By.ID, "Disconnect")))
        driver.close()
        frames.clear()
        print("Done changIP")

        # lock.acquire()

        # thread3 = myThread3("https://www.facebook.com/", Phone[2],
        #                     password, random.choice(First_name), random.choice(last_name), random.choice(user_agent_list), random.choice(locales))
        # thread4 = myThread4("https://www.facebook.com/", Phone[3],
        #                     password, random.choice(First_name), random.choice(last_name), random.choice(user_agent_list), random.choice(locales))
        # thread5 = myThread5("https://www.facebook.com/", Phone[4],
        #                     password, random.choice(First_name), random.choice(last_name), random.choice(user_agent_list), random.choice(locales))
        # lock.acquire()
        thread1.start()
        Join.append(thread1)
        thread2.start()
        Join.append(thread1)
        # thread3.start()
        # Join.append(thread1)
        # thread4.start()
        # Join.append(thread1)
        # thread5.start()
        # Join.append(thread1)
        thread1.join()
        thread2.join()
        # lock.release()
        print("done")
        Phone.clear()
        Join.clear()
