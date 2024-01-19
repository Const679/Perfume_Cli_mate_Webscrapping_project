
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
import os
import winreg
from zipfile import ZipFile
warnings.filterwarnings("ignore")
import json

options = EdgeOptions()
options.use_chromium = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.set_capability("acceptInsecureCerts", True)
options.binary_location =r'C:\Users\fouzari\Desktop\web_scrapp\driverEdge\msedgedriver_v133.exe'

def Sephora():
    dicParfum={}
    listeMarque=[]
    listeIngredient=[]
    driver = Edge(executable_path =r"C:\Users\fouzari\Desktop\web_scrapp\driverEdge\msedgedriver_v133.exe")
    driver.get("https://www.sephora.fr/")
    cookies=driver.find_element(By.XPATH,'//*[@id="footer_tc_privacy_button_2"]')
    cookies.click()
    i=0 #placement sur la page web
    key=0 #classement
    while key<10:
        div=0
        driver.get("https://www.sephora.fr/parfum-meilleures-ventes/?srule=Sorting%20Rule%20-%20Best%20Sellers&start=0&sz=24")
        id=str(i+1)
        try:
            pathparfum="/html/body/div[2]/div[3]/div[2]/div[3]/div[2]/div[2]/ul/li["+id+"]"
            Parfum=driver.find_element(By.XPATH, pathparfum)
        except :
            pathparfum="/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]/ul/li["+id+"]"
            Parfum=driver.find_element(By.XPATH, pathparfum)
        if Parfum.get_attribute('class')=='grid-tile':
            key+=1
            marque=driver.find_element(By.XPATH,pathparfum+"/div/div[3]/div/a/span").get_attribute('innerText')
            #print(marque)
            listeMarque.append(marque)
            Parfum.click()
            #nom du parfum      
            nomParfum=driver.find_element(By.CLASS_NAME,'product-name.product-name-bold').get_attribute("innerText")
            #print(nomParfum)
            dicParfum[key]=nomParfum
            #liste des ingredients
            ingredient=driver.find_element(By.ID,'tab-ingredients').click()
            time.sleep(1)
            liste_I=driver.find_element(By.CLASS_NAME,"ingredients-content").get_attribute('innerText')
            #print('Ingredient : '+ ingredient)
            listeIngredient.append(liste_I)
            #print("\n")
        i+=1
            
    driver.close()
    return dicParfum,listeMarque,listeIngredient
dicParfum,listeMarque,listeIngredient=Sephora()

def IngredientForme(listeIngredient):
    phrase="Cette liste d'ingrédients peut faire l'objet de modifications, veuillez consulter l'emballage du produit acheté."
    Ingredient=[]
    for i in listeIngredient:
        ouisticram=i.replace("\n",'')
        ouisticram=ouisticram.replace(phrase,'')
        ousticram=ouisticram.replace(phrase,'')
        if "INGREDIENTS" in ouisticram:
            champenfeu=ouisticram.split(':')
            champenfeu=champenfeu[-1]
        else:
            champenfeu=ouisticram
        if "●" in champenfeu :
            simiabraz=champenfeu.split("●")
        elif " | " in champenfeu:
            simiabraz=champenfeu.split(" | ")
        elif ' ,' in champenfeu:
            simiabraz=champenfeu.split(" ,")
        elif ',' in champenfeu:
            simiabraz=champenfeu.split(",")
        elif " • " in champenfeu:
            simiabraz=champenfeu.split(" • ")
        else:
            print(simiabraz)
        Ingredient.append(simiabraz)


    Ingredients=[]
    for i in Ingredient:
        for j in i :
            if j.startswith('#'):
                ij=j.split(' ')
                j=ij[1]
            if j.startswith(' '):
                j=j[1:]
            if j.endswith(' '):
                j=j[:-1]
            Ingredients.append(j)
    
    setIngredient=set(Ingredients)
    return setIngredient
setIngredient=IngredientForme(listeIngredient)


 
def incibeauty(setIngredient):
    descIng={}
    Allergene=[]
    endo=[]
    driver = Edge(executable_path =r"C:\Users\fouzari\Desktop\web_scrapp\driverEdge\msedgedriver_v133.exe")
    driver.get("https://incibeauty.com/ingredients")
    cookies=driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/button")
    cookies.click()
    for i in setIngredient:
        driver.get("https://incibeauty.com/ingredients")
        search=driver.find_element(By.ID,'searchInci')
        search.click()
        search.clear()
        search.send_keys(i)
        count=0
        url=False
        b=True
        while b:
            count+=1
            search.send_keys(Keys.ENTER)
            if driver.current_url!="https://incibeauty.com/ingredients":
                b=False
                url=True
            if count>=10:
                b=False
        if url :
            listeInfo= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/section[1]/div/div/div/ul')))
            if 'Allergène' in listeInfo.get_attribute('innerText'):
                Allergene.append(i)
            if 'Perturbateur endocrinien' in listeInfo.get_attribute('innerText'):
                endo.append(i)
            try:
                aSavoir=driver.find_element(By.XPATH,'/html/body/section[1]/div/div/div/div[2]/div')
                descIng[i]=aSavoir.get_attribute('innerText')
            except:
                descIng[i]="Pas d'information supplémentaire"

    driver.close()
    return descIng,Allergene,endo

 
def engagement(listeMarque):
    marqueEco={}
    driver = Edge(executable_path =r"C:\Users\fouzari\Desktop\web_scrapp\driverEdge\msedgedriver_v133.exe")
    driver.get("https://sciencebasedtargets.org/companies-taking-action#dashboard")
    time.sleep(5)
    cookies=driver.find_element(By.CLASS_NAME,"font-bold.text-center.rounded-full.appearance-none.o-btn.border-3.border-currentColor.flex-shrink-0.is-current")
    cookies.click()
    #recherche la marque
    inputs=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/label/input")
                                         #/html/body/main/div/div[3]/div[2]/div/div/div/div[1]/div/div[2]/label/input
    for i in listeMarque:
        inputs.send_keys(i)
        time.sleep(5)
        try :
            #click sur view more pour avoir accès à la target
            driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/label/span/span").click()
            target=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[2]").get_attribute("innerText")
            marqueEco[i]=target
        except:
            marqueEco[i]="Sans engagement"
        inputs.clear()
    driver.close()
    return marqueEco

descIng,Allergene,endo=incibeauty(setIngredient)
marqueEco=engagement(listeMarque)

def create_json(dicParfum, listeMarque, setIngredient, descIng, Allergene, endo, marqueEco):
    json_structure = {
        "SephoraData": {
            "Perfumes": dicParfum,
            "Brands": listeMarque
        },
        "Ingredients": {
            "SetIngredient": list(setIngredient),
            "Descriptions": descIng,
            "Allergens": Allergene,
            "EndocrineDisruptors": endo
        },
        "BrandEngagements": marqueEco
    }

    with open('output_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_structure, json_file, ensure_ascii=False, indent=4)