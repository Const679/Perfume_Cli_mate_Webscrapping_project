import pandas as pd
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import re
import time
import warnings
warnings.filterwarnings("ignore")

options = EdgeOptions()
options.use_chromium = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.set_capability("acceptInsecureCerts", True)
#options.add_argument('headless') #hide the browser
#Try to connect if the edgeriver version is 108
options.binary_location =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

def Engagement(marque,options):
    driver = Edge(executable_path =r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe", options = options)
    driver.get("https://sciencebasedtargets.org/companies-taking-action#dashboard")
    time.sleep(5)
    cookies=driver.find_element(By.CLASS_NAME,"font-bold.text-center.rounded-full.appearance-none.o-btn.border-3.border-currentColor.flex-shrink-0.is-current")
    cookies.click()
    #recherche la marque
    inputs=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/label/input")
    inputs.send_keys(marque)
    time.sleep(5)
    try :
        #click sur view more pour avoir accès à la target
        driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/label/span/span").click()
        target=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]").get_attribute("innerText")
    except:
        target="Sans engagement"
    driver.close()
    return target

def parfumPerso (nomP,options):
    nomP=nomP.replace(' ','+')
    driver = Edge(executable_path =r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe", options = options)
    driver.get("https://www.sephora.fr/on/demandware.store/Sites-Sephora_FR-Site/fr_FR/Search-AlgoliaSearch?q="+nomP+"&categories=Eau+de+parfum%7CC297810")
    cookies=driver.find_element(By.XPATH,'//*[@id="footer_tc_privacy_button_2"]')
    cookies.click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div/div/div/div/ol/li[1]/div/div[2]/a").click()
    lamarque=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span").get_attribute('innerText')
    ingredient=driver.find_element(By.ID,'tab-ingredients').click()
    time.sleep(1)
    lesingredients=driver.find_element(By.CLASS_NAME,"ingredients-content").get_attribute('innerText')
    driver.close()
    lengagement=Engagement(lamarque,options)
    return lamarque,lesingredients,lengagement

#print(parfumPerso('hugo boss',options))




