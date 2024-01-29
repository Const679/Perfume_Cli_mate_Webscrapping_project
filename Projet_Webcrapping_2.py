from selenium import webdriver
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions
import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from Projet_Webcrapping_2 import * 
from web_const_mod import * 
from msedge.selenium_tools import Edge, EdgeOptions
import warnings
import os
import time
import winreg
import json
from zipfile import ZipFile
warnings.filterwarnings("ignore")

#Fonction de recher de l'engagement d'un marque
def Engagement(marque,options,executablePath):
    #Ouvre la navigateur et va sur le site sciense based targets
    driver = Edge(executable_path =executablePath, options = options)
    driver.get("https://sciencebasedtargets.org/companies-taking-action#dashboard")
    time.sleep(5)
    #Accepte les cookies
    try:
        cookies=driver.find_element(By.CLASS_NAME,"font-bold.text-center.rounded-full.appearance-none.o-btn.border-3.border-currentColor.flex-shrink-0.is-current")
        cookies.click()
    except :
        "pas de cookies"
    #recherche la marque
    inputs=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/label/input")
    inputs.send_keys(marque)
    time.sleep(5)
    #Si la marque est présente sur le site alors récupere le texte de Target
    try :
        #click sur view more pour avoir accès à la target
        driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/label/span/span").click()
        target=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]").get_attribute("innerText")
    #Sinon l'entreprise est considéré comme n'ayant pas d'engagement
    except:
        target="Sans engagement"
    driver.close()
    return target

#Fonction qui récupère toute les informations d'un parfum donné
def parfumPerso (nomP,options,executablePath):
    #Met en forme le nom du parfum pour l'entrer dans un URL
    nomP=nomP.replace(' ','+')
    #Ouvre le navigateur et va sur le site de Sephora avec la recherche lié au nom du parfum
    driver = Edge(executable_path =executablePath, options = options)
    driver.get("https://www.sephora.fr/on/demandware.store/Sites-Sephora_FR-Site/fr_FR/Search-AlgoliaSearch?q="+nomP+"&categories=Parfum%7CC301")
    get=driver.current_url
    if 'NoHits?' in get:
        driver.get("https://www.sephora.fr/on/demandware.store/Sites-Sephora_FR-Site/fr_FR/Search-AlgoliaSearch?q="+nomP+"&categories=Eau+de+parfum%7CC297818")
    #Continue sans accepter les cookies
    cookies=driver.find_element(By.XPATH,'//*[@id="footer_tc_privacy_button_2"]')
    cookies.click()
    time.sleep(2)
    #Selectionne le premier parfum de la page
    driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/div/div/div/div/ol/li[1]/div/div[2]/a").click()
    #recupère la marque du parfum
    lamarque=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/a/span").get_attribute('innerText')
    #Ouvre la liste des ingrédients
    driver.find_element(By.ID,'tab-ingredients').click()
    time.sleep(1)
    #Recupère les ingrédients
    lesingredients=driver.find_element(By.CLASS_NAME,"ingredients-content").get_attribute('innerText')
    driver.close()
    #Recherche les engagement de la marque
    lengagement=Engagement(lamarque,options,executablePath)
    return lamarque,lesingredients,lengagement
