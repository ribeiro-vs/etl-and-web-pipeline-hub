from verifiers import process_registrant
from plconfig import SecInfo as sec 
from playwright.sync_api import sync_playwright 
import time
import json
from reports import MReport02 as rep
import pyperclip
import pyautogui
import os
from datetimetools import Alternative_date_variables

"""
    It is strictly for the purposes of:
        - Managing the behaviour of the web actions across each platform.
"""

class BrowserInitiator:

    def __init__(self):
        self.browser=None
        self.context=None
        self.page=None
        self.cookies=sec()
        self.link=sec()

    def start_browser(self,p): 
        self.browser = p.chromium.launch(headless=False)
        self.context = self.browser.new_context(accept_downloads=True)
        self.context.add_cookies(self.cookies_json)
        self.page = self.context.new_page()
        self.page.goto(self.link)
    
    def start_browser_new_context(self,p):  
        self.browser = p.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto(self.link)
        pyautogui.getWindowsWithTitle("Chromium")[0].maximize()

    def cookies_identifier(self,method):
        if   method.__name__=='extract_mb_data' or method.__name__=='authenticate_metabase':
            return self.cookies.mb_cookies
        elif method.__name__=='extract_gs_data' or method.__name__=='authenticate_gsheets':
            return self.cookies.gs_cookies
        elif method.__name__=='extract_zk_data' or method.__name__=='authenticate_zendesk':
            return self.cookies.zk_cookies
        elif method.__name__=='extract_lg_data' or method.__name__=='authenticate_lg':
            return self.cookies.lg_cookies
        elif method.__name__=='generate_lg_data':
            return self.cookies.lg_cookies

    def load_cookies(self,method=None):
        with open(self.cookies_identifier(method),'r') as f:
            self.cookies_json = json.load(f)
            
    def close_browser(self):
        if self.browser:
            self.browser.close()

class Authenticator():

    def __init__(self,browser_initiator):
        self.link = sec()
        self.credentias = sec()
        self.browser_initiator = browser_initiator

    def fill(self,value):
        self.browser_initiator.page.wait_for_load_state('load')
        time.sleep(5)
        pyperclip.copy(value)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.hotkey("enter")
        time.sleep(7)

    def click_to_log_in(self,button):
        try:  
            self.browser_initiator.page.wait_for_load_state('load')
            self.browser_initiator.page.wait_for_selector(button,timeout=(15*1000))
            self.browser_initiator.page.click(button)
            self.browser_initiator.page.wait_for_load_state('load')
        except Exception as e:
            pass
    
    def save_cookies(self,func):
        cookie = self.browser_initiator.cookies_identifier(func)
        try:
            cookies = self.browser_initiator.context.cookies()
            with open(cookie, 'w') as f:
                json.dump(cookies, f)
        except Exception as e:
            process_registrant.register_info('save_cookies from Authenticator: '+str(e))  

    def authenticate_metabase(self):
        try:
            self.browser_initiator.link=sec()
            self.browser_initiator.link=self.browser_initiator.link.mb_url
            with sync_playwright() as p: 
                self.browser_initiator.start_browser_new_context(p)
                self.click_to_log_in('[class="AuthButtonstyled__CardText-j2pohn-3 gAbWId"]')
                self.fill(self.credentias.xusr) 
                self.fill(self.credentias.xpss)
                self.browser_initiator.page.wait_for_load_state('load')
                time.sleep(60)
                self.save_cookies(self.authenticate_metabase)
                self.browser_initiator.close_browser()
            self.browser_initiator.link = ''
        except Exception as e:
            process_registrant.register_error('authenticate_metabase from Authenticator: '+str(e))

    def authenticate_gsheets(self):
        try:
            self.browser_initiator.link=sec()
            self.browser_initiator.link=self.browser_initiator.link.gs_url
            with sync_playwright() as p: 
                self.browser_initiator.start_browser_new_context(p)
                self.browser_initiator.page.wait_for_load_state('load')
                time.sleep(1)
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                self.fill(self.credentias.xusr)
                self.fill(self.credentias.xpss) 
                time.sleep(60)
                self.save_cookies(self.authenticate_gsheets)
                self.browser_initiator.close_browser()
            self.browser_initiator.link = ''
        except Exception as e:
            process_registrant.register_error('authenticate_gsheets from Authenticator: '+str(e))

    def authenticate_zendesk(self):
        try:
            self.browser_initiator.link=sec()
            self.browser_initiator.link = self.browser_initiator.link.zk_url
            with sync_playwright() as p:
                self.browser_initiator.start_browser_new_context(p)
                pyautogui.getWindowsWithTitle("Chromium")[0].maximize()
                self.browser_initiator.page.wait_for_load_state('load')
                time.sleep(1)
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                pyautogui.hotkey("tab")
                self.fill(self.credentias.zusr)
                self.fill(self.credentias.zpss)  
                self.save_cookies(self.authenticate_zendesk) 
                self.browser_initiator.close_browser()
            self.browser_initiator.link = ''
        except Exception as e:
            process_registrant.register_error('authenticate_zendesk from Authenticator: '+str(e))

    def authenticate_lg(self):
        self.browser_initiator.link=sec()
        self.browser_initiator.link = self.browser_initiator.link.lg_url
        with sync_playwright() as p:
            self.browser_initiator.start_browser_new_context(p) 
            pyautogui.getWindowsWithTitle("Chromium")[0].maximize()         
            pyautogui.hotkey("tab")
            pyautogui.hotkey("tab")
            pyautogui.hotkey("tab")
            pyautogui.hotkey("tab")
            self.fill(self.credentias.yusr)
            self.fill(self.credentias.ypss) 
            time.sleep(10)
            self.save_cookies(self.authenticate_lg)
            self.browser_initiator.close_browser()
        self.browser_initiator.link = ''

class Extractor():

    def __init__(self,time,link,path): 
        self.time = time 
        self.link = link
        self.path = path
        self.format = os.path.splitext(self.path[0])
        self.browser_initiator=BrowserInitiator()
        self.authenticator=Authenticator(self.browser_initiator)  

    def extract_mb_data(self): 

        with sync_playwright() as p:

            self.browser_initiator.link=self.link
            # Identifies the right cookie for the class method
            self.browser_initiator.load_cookies(self.extract_mb_data)
            # Opens page
            self.browser_initiator.start_browser(p) 

            # Clicks google login button
            button='[class="AuthButtonstyled__CardLink-j2pohn-1 kTRzbu AuthButtonstyled__TextLink-j2pohn-0 eNUpTi Link-sc-120rwae-0 brZxup"]'
            self.authenticator.click_to_log_in(button)
    
            # Clicks download button
            button = '[class="Icon Icon-download Icon__StyledIcon-oj89wd-1 boNzPM"]'
            self.browser_initiator.page.wait_for_selector(button,timeout=(self.time*1000)) 
            self.browser_initiator.page.click(button)  

            # chooses format option
            if self.format[1] == '.csv':
                download = '[class="text-white-hover bg-brand-hover rounded cursor-pointer full hover-parent hover--inherit sc-bwzfXH iTgcwE"]' 
            else:
                download = '[class="Icon Icon-xlsx Icon__StyledIcon-oj89wd-1 eZysOH"]' 

            # Waits for downlaod based on time limit of the report
            with self.browser_initiator.page.expect_download(timeout=(self.time*1000)) as download_info:
                self.browser_initiator.page.wait_for_selector(download) 
                self.browser_initiator.page.click(download,timeout=(self.time*1000))

            download = download_info.value

            for each in self.path: 
                download.save_as(each)

            self.authenticator.save_cookies(self.extract_mb_data)

            self.browser_initiator.link = ''
            
            self.browser_initiator.close_browser() 

    def extract_gs_data(self): 

        with sync_playwright() as p:

            self.browser_initiator.link=self.link
            self.browser_initiator.load_cookies(self.extract_gs_data)
            self.browser_initiator.start_browser(p) 

            pyautogui.getWindowsWithTitle("Chromium")[0].maximize()

            button='#docs-file-menu'
            self.authenticator.click_to_log_in(button)
            
            time.sleep(20)

            pyautogui.click(160,369)

            if   self.format[1] == '.csv':
                pyautogui.click(414,497)
            elif self.format[1] == '.tsv':
                pyautogui.click(416,536)
            else:
                pyautogui.click(416,374)  

            with self.browser_initiator.page.expect_download(timeout=(self.time*1000)) as download_info: 

                download = download_info.value

            for each in self.path:
                download.save_as(each)

            self.authenticator.save_cookies(self.extract_gs_data)

            self.browser_initiator.link = ''

            self.browser_initiator.close_browser()
    
    def extract_zk_data(self): 

        with sync_playwright() as p:

            self.browser_initiator.link=self.link
            self.browser_initiator.load_cookies(self.extract_zk_data)
            self.browser_initiator.start_browser(p) 

            pyautogui.getWindowsWithTitle("Chromium")[0].maximize()

            time.sleep(8)
 
            self.authenticator.click_to_log_in('[class="StyledIcon-sc-19meqgg-0 hkQnhl"]') 
            try:
                self.authenticator.click_to_log_in('[id="downshift-0-item-3"]') 
                time.sleep(3)
                self.authenticator.click_to_log_in('[id="downshift-0-item-3"]') 
                self.authenticator.click_to_log_in('[id="downshift-0-item-3"]') 
            except:
                pass
            self.authenticator.click_to_log_in('[id="4val-field_2.1.2--label"]') 
            self.authenticator.click_to_log_in('[id="4val-field_2.1.2--label"]') 
            self.authenticator.click_to_log_in('[id="2val-field_2.1.2--label"]')
            

            download='[class="StyledButton-sc-qe3ace-0 ilhaiR"]'

            with self.browser_initiator.page.expect_download(timeout=(self.time*1000)) as download_info:
                self.browser_initiator.page.wait_for_selector(download) 
                self.browser_initiator.page.click(download,timeout=(self.time*1000))

            download = download_info.value

            for each in self.path:
                download.save_as(each)

            self.authenticator.save_cookies(self.extract_zk_data)

            self.browser_initiator.link = ''

            self.browser_initiator.close_browser()

    def generate_lg_data(self): 

        with sync_playwright() as p:

            self.browser_initiator.link=self.link
            self.browser_initiator.load_cookies(self.generate_lg_data)
            self.browser_initiator.start_browser(p) 

            sta=Alternative_date_variables().past_month_first_day_dd_mm_yyyy_with_slash
            end=Alternative_date_variables().current_month_last_day_dd_mm_yyyy_with_slash

            pyautogui.getWindowsWithTitle("Chromium")[0].maximize()

            self.authenticator.click_to_log_in('text=Frequência')
            time.sleep(15)
            pyautogui.click(451,186)
            time.sleep(10)
            pyautogui.click(83,499)
            time.sleep(10)
            pyautogui.click(256,540)
            time.sleep(10)
            pyautogui.click(259,250)
            time.sleep(10)
            pyautogui.click(190,336)
            time.sleep(10)
            pyautogui.click(345,355)
            time.sleep(10)
            pyautogui.click(342,411)
            time.sleep(10)
            pyautogui.click(664,735)
            time.sleep(10)
            pyautogui.click(1104,291)
            time.sleep(10)
            pyautogui.click(172,326)  
            time.sleep(10)
            pyautogui.click(335,733) 
            time.sleep(10)
            self.authenticator.fill(sta) 
            pyautogui.hotkey("tab")
            time.sleep(10)
            self.authenticator.fill(end)
            pyautogui.click(83,499)
            time.sleep(10)
            pyautogui.click(868,690)
            time.sleep(10)

            self.browser_initiator.link = '' 
            self.browser_initiator.close_browser()
