from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import random
import mechanize
from shutil import which
import requests
import json
import requests_async as requests_asy



langs = []


class Facebook_bot():
    def __init__(self,  url, telephones, passwords, first_names, last_names, url_ip, uername_ip, password_ip, user_agent,locale):

        self.Sign_up(url, telephones, passwords, first_names,
                     last_names, user_agent,locale)

    def Sign_up( url, telephones, passwords, first_names, last_names, user_agent,locale):
        try:
            # self.change_ip(url_ip, uername_ip, password_ip)
            options = Options()
            options.headless = True
            localtime = time.localtime(time.time())
            print(localtime)
            r = random.randint(20, 40)
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.privatebrowsing.autostart',True)
            profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)
            profile.set_preference("media.peerconnection.enabled", False)
            profile.set_preference("general.useragent.override", user_agent)
            profile.set_preference("browser.download.folderList",2)
            profile.set_preference("browser.download.manager.showWhenStarting",False)
            profile.set_preference("browser.download.dir", "/home/ducdev/Desktop/CreateFacebook/profile")
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
            profile.set_preference("intl.accept_languages", locale)
            profile.update_preferences()

            firefox_dev_binary = FirefoxBinary(
                "/home/ducdev/Desktop/CreateFacebook/firefox-80.0b3/firefox/firefox")
            driver = webdriver.Firefox(
                firefox_profile=profile, firefox_binary= firefox_dev_binary,firefox_options=options
                )
            print("profile",profile)
            driver.get("https://vi-vn.facebook.com/")
            items = driver.find_element_by_xpath(
                "//ul[@class = 'uiList localeSelectorList _2pid _509- _4ki _6-h _6-j _6-i']")
            lang = items.find_elements_by_tag_name("li")
            for pri_lang in lang:
                langs.append(pri_lang)

            lang_choice = random.choice(langs[:1])
            time.sleep(2)
            lang_choice.click()
            time.sleep(2)
            first_name =driver.find_elements_by_id("u_0_m")
            time.sleep(2)
            first_name[0].click()
            print(first_name)
            for first_namess in first_names:
                time.sleep(0.5)
                first_name[0].send_keys(first_namess)
            time.sleep(2)
            last_name = driver.find_elements_by_id("u_0_o")
            time.sleep(3)
            last_name[0].click()
            for last_namess in last_names:
                time.sleep(0.5)
                last_name[0].send_keys(last_namess)
            time.sleep(2)
            telephone = driver.find_elements_by_id("u_0_r")
            time.sleep(4)
            telephone[0].click()
            for telephoness in telephones:
                time.sleep(0.7)
                telephone[0].send_keys(telephoness)
            time.sleep(2)
            password = driver.find_elements_by_id("password_step_input")
            time.sleep(2.2)
            password[0].click()
            for passwordss in passwords:
                time.sleep(0.5)
                password[0].send_keys(passwordss)
            time.sleep(2)
            day = Select(driver.find_element_by_id('day'))
            print("day", day)
            day_now = localtime[2]
            day_select = day_now
            print("day", day_select)
            time.sleep(4)
            day.select_by_visible_text(str(day_select))
            time.sleep(2)
            month = Select(driver.find_element_by_id('month'))
            moth_now = localtime[1]
            moth_select = localtime[1]-2
            time.sleep(4)
            month.select_by_value(str(moth_select))
            time.sleep(2)
            year = Select(driver.find_element_by_id("year"))
            year_now = localtime[0]
            year_select = year_now - r
            time.sleep(3)
            year.select_by_value(str(year_select))

            if localtime[3] % 2 == 0:
                time.sleep(2)
                sex_male = driver.find_elements_by_css_selector(
                    "input[type='radio'][value='1']")[0]
                time.sleep(4)
                sex_male.click()
            else:
                time.sleep(2)
                sex_female = driver.find_elements_by_css_selector(
                    "input[type='radio'][value='2']")[0]
                time.sleep(4)
                sex_female.click()
            time.sleep(2.7)
            sign_up = driver.find_element_by_id("u_0_13")
            time.sleep(4)
            sign_up.click()
            time.sleep(15)
            element = driver.find_elements_by_id("code_in_cliff")
            print(element)
            if element != []:
                # Client = http3.AsyncClient()
                # r = await client.get('https://www.example.org/')
                chang_tele = driver.find_elements(
                    By.XPATH, '//*[@class ="_42ft _4jy0 _8iu3 _4jy4 _517h _51sy"]')
                time.sleep(2)

                chang_tele[0].click()
                time.sleep(3.5)
                response = requests.get(
                    'https://server.nanosim.vn/api/ig/request?api_token=AnQNCRb7nela0OV0nv9B&serviceId=19')
                content = response.content
                a = json.loads(content)
                sessionId = a["data"].get("session_id")
                phone = a["data"].get("phone")
                print(a["data"])
                input_SMS = driver.find_elements(
                    By.XPATH, "//*[@class = 'inputtext _8n1_']")
                time.sleep(3)
                input_SMS[0].click()
                for phones in phone:
                    time.sleep(0.5)

                    input_SMS[0].send_keys(phones)
                time.sleep(3)
                btn_confirm = driver.find_elements(
                    By.XPATH, "//*[@class ='_42ft _4jy0 layerConfirm _8n28 _8n2a uiOverlayButton _4jy3 _4jy1 selected _51sy']")
                time.sleep(3.5)
                btn_confirm[0].click()

                print("sessionId", sessionId)
                time.sleep(120)
                url_get_SMS = "https://server.nanosim.vn/api/ig/code?api_token=AnQNCRb7nela0OV0nv9B&sessionId=" + \
                    str(sessionId)
                print("url", url_get_SMS)
                SMS = requests.get(str(url_get_SMS))
                content1 = SMS.content
                b = json.loads(content1)
                print(b['data'])
                SMS_Id = b["data"].get("sms")

                ID_SMS = driver.find_elements_by_id("code_in_cliff")
                time.sleep(2.5)
                ID_SMS[0].click()
                print("SMS", SMS_Id[:5])
                for SMS_Ids in SMS_Id[:5]:
                    time.sleep(0.5)
                    ID_SMS[0].send_keys(SMS_Ids)
                time.sleep(2.5)
                btn_continue = driver.find_elements(
                    By.XPATH, "//*[@class='_42ft mls _4jy0 _8iu3 _8iu6 _4jy4 _4jy1 selected _51sy']")
                time.sleep(2)
                btn_continue[0].click()
                time.sleep(5)
                # divofok = pam uiOverlayFooter uiBoxGray topborder
                # ok = _42ft _42fu layerCancel uiOverlayButton selected _42g- _42gy

                btn_ok = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, "_42ft _42fu layerCancel uiOverlayButton selected _42g- _42gy")))
                btn_oks = driver.switch_to.alert
                print("btn_ok", btn_ok)
                if btn_oks != []:

                    print("btn_ok", btn_ok)
                    time.sleep(2.5)
                    btn_oks.accept()
                else:
                    self.driver.close()
                # tiep_tuc = fbnux-next-navbutton
            else:
                driver.close()


            # response = requests.get('https://server.nanosim.vn/api/ig/request?api_token=AnQNCRb7nela0OV0nv9B&serviceId=19')
            # print(response.status_code)

        except:
            driver.close()

    def change_user_agent(self, url, user_agent):
        try:

            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = user_agent
            page = browser.open(url)
            source_code = page.read()

            print(source_code)
        except:
            print("Error in browsing.....")
